## -*- coding: utf-8 -*-

import copy
import math

# Math consts
M_PI = 3.1415926535897932384626433832795
F_G = 9.81
M_E = 2.71828182845904523536
H_LEET = 1337

# Defines
MAX_EXPR_LEN = 255
MAX_TOKEN_LEN = 80

# Brackets
CALC_END = -1
CALC_L_BRACKET = -2
CALC_R_BRACKET = -3
CALC_NUMBER = -4

# Operations
OP_PLUS = 0
OP_MINUS = 1
OP_MULTIPLY = 2
OP_DIVIDE = 3
OP_PERCENT = 4
OP_POWER = 5
OP_UMINUS = 6

# Math Operations
OP_SIN = 7
OP_COS = 8
OP_TG = 9
OP_CTG = 10
OP_ARCSIN = 11
OP_ARCCOS = 12
OP_ARCTG = 13
OP_ARCCTG = 14
OP_SH = 15
OP_CH = 16
OP_TH = 17
OP_CTH = 18
OP_EXP = 19
OP_LG = 20
OP_LN = 21
OP_SQRT = 22
OP_IN = 23
CALC_PI = 24
CALC_G = 25
CALC_LEET = 26

TERMINATOR = "\x00"


def strlen(list1):
    list1 = list(list1)
    i = 0
    while list1[i] != TERMINATOR:
        i = i + 1
    return i

def strcmp(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    total = len(list1) if len(list1) < len(list2) else len(list2)
    for i in range(0, total):
        if i > len(list1) - 1:
            return not True
        elif i > len(list2):
            return not True
        elif list1[i] != list2[i]:
            return not False
        else:
            continue


def atof(text):
    text = "".join(text[:strlen(text)])
    integer = int(text)
    double = float(text)
    if integer == double:
        return integer
    else:
        return double


class TCALCNode():
    value = 0
    left = None
    right = None

    def __init__(self, _value=0, _left=None, _right=None):
        self.left = _left
        self.right = _right
        self.value = _value


class TCALC():
    root = None
    expr = [TERMINATOR for i in range(0, MAX_EXPR_LEN)]
    curToken = [TERMINATOR for i in range(0, MAX_TOKEN_LEN)]
    typToken = 0
    pos = 0
    result = 0

    def IsDelim(self):
        for char in list("+-*/%^()[]"):
            if self.expr[self.pos] == char:
                return True
            else:
                continue
        return False

    def IsLetter(self):
        return ((ord(self.expr[self.pos]) >= ord('a') and ord(self.expr[self.pos]) <= ord('z')) or (
                ord(self.expr[self.pos]) >= ord('A') and ord(self.expr[self.pos]) <= ord('Z')))

    def IsDigit(self):
        return (ord(self.expr[self.pos]) >= ord('0') and ord(self.expr[self.pos]) <= ord('9'))

    def IsPoint(self):
        return self.expr[self.pos] == "."

    def GetToken(self):
        self.curToken[0] = TERMINATOR
        while self.expr[self.pos] == " ":
            self.pos = self.pos + 1
        if self.expr[self.pos] == TERMINATOR:
            self.curToken[0] = TERMINATOR
            self.typToken = CALC_END
            return True
        elif self.IsDelim():
            choose_dict = {
                "+" : OP_PLUS,
                "-" : OP_MINUS,
                "*" : OP_MULTIPLY,
                "/" : OP_DIVIDE,
                "%" : OP_PERCENT,
                "[" : CALC_L_BRACKET,
                "(" : CALC_L_BRACKET,
                "]" : CALC_R_BRACKET,
                ")" : CALC_R_BRACKET,

            }
            self.curToken[0] = self.expr[self.pos]
            self.pos = self.pos + 1
            self.curToken[1] = TERMINATOR
            tmp = "".join(self.curToken[:strlen(self.curToken)])
            
            if tmp in choose_dict:
                self.typToken = choose_dict[tmp]
                return True
            
        elif self.IsLetter():
            i = 0
            while self.IsLetter():
                self.curToken[i] = self.expr[self.pos]
                self.pos = self.pos + 1
                i = i + 1
            self.curToken[i] = TERMINATOR
            len = strlen(self.curToken)
            for i in range(0, len):
                if ord(self.curToken[i]) >= ord('A') and ord(self.curToken[i]) <= ord('Z'):
                    self.curToken[i] = chr(ord(self.curToken[i]) + ord('a') - ord('A'))
            if not strcmp(self.curToken, list("leet")):
                self.typToken = CALC_LEET
                return True
            elif not strcmp(self.curToken, list("g")):
                self.typToken = CALC_G
                return True
            elif not strcmp(self.curToken, list("pi")):
                self.typToken = CALC_PI
                return True
            elif not strcmp(self.curToken, list("sin")):
                self.typToken = OP_SIN
                return True
            elif not strcmp(self.curToken, list("cos")):
                self.typToken = OP_COS
                return True
            elif not strcmp(self.curToken, list("tg")):
                self.typToken = OP_TG
                return True
            elif not strcmp(self.curToken, list("ctg")):
                self.typToken = OP_CTG
                return True
            elif not strcmp(self.curToken, list("arcsin")):
                self.typToken = OP_ARCSIN
                return True
            elif not strcmp(self.curToken, list("arccos")):
                self.typToken = OP_ARCCOS
                return True
            elif not strcmp(self.curToken, list("sh")):
                self.typToken = OP_SH
                return True
            elif not strcmp(self.curToken, list("ch")):
                self.typToken = OP_CH
                return True
            elif not strcmp(self.curToken, list("th")):
                self.typToken = OP_TH
                return True
            elif not strcmp(self.curToken, list("cth")):
                self.typToken = OP_CTH
                return True
            elif not strcmp(self.curToken, list("exp")):
                self.typToken = OP_EXP
                return True
            elif not strcmp(self.curToken, list("lg")):
                self.typToken = OP_LG
                return True
            elif not strcmp(self.curToken, list("ln")):
                self.typToken = OP_LN
                return True
            elif not strcmp(self.curToken, list("sqrt")):
                self.typToken = OP_SQRT
                return True
            else:
                self.SendError(0)
        elif self.IsDigit() or self.IsPoint():
            i = 0
            while self.IsDigit():
                self.curToken[i] = self.expr[self.pos]
                self.pos = self.pos + 1
                i = i + 1
            if self.IsPoint():
                self.curToken[i] = self.expr[self.pos]
                self.pos = self.pos + 1
                i = i + 1
                while self.IsDigit():
                    self.curToken[i] = self.expr[self.pos]
                    self.pos = self.pos + 1
                    i = i + 1
            self.curToken[i] = TERMINATOR
            self.typToken = CALC_NUMBER
            return True
        else:
            self.curToken[0] = self.expr[self.pos]
            self.pos = self.pos + 1
            self.curToken[1] = TERMINATOR
            self.SendError(1)
        return False

    def CreateNode(self, _value, _left, _right):
        return TCALCNode(_value, _left, _right)

    def Expr(self):
        temp = self.Expr1()
        while True:
            if self.typToken == OP_PLUS:
                self.GetToken()
                temp = self.CreateNode(OP_PLUS, temp, self.Expr1())
            elif self.typToken == OP_MINUS:
                self.GetToken()
                temp = self.CreateNode(OP_MINUS, temp, self.Expr1())
            else:
                break
        return temp

    def Expr1(self):
        temp = self.Expr2()
        while True:
            if self.typToken == OP_MULTIPLY:
                self.GetToken()
                temp = self.CreateNode(OP_MULTIPLY, temp, self.Expr2())
            elif self.typToken == OP_DIVIDE:
                self.GetToken()
                temp = self.CreateNode(OP_DIVIDE, temp, self.Expr2())
            elif self.typToken == OP_PERCENT:
                self.GetToken()
                temp = self.CreateNode(OP_PERCENT, temp, self.Expr2())
            else:
                break
        return temp

    def Expr2(self):
        temp = None
        if self.typToken == OP_PLUS:
            self.GetToken()
            temp = self.Expr3()
        elif self.typToken == OP_MINUS:
            self.GetToken()
            temp = self.CreateNode(OP_UMINUS, self.Expr3(), None)
        else:
            temp = self.Expr3()
        return temp

    def Expr3(self):
        temp = None
        if self.typToken >= OP_SIN and self.typToken <= OP_SQRT + 1:
            temp = self.CreateNode(OP_SIN - OP_SIN + self.typToken, None, None)
            self.GetToken()
            if self.typToken != CALC_L_BRACKET:
                self.SendError(4)
            self.GetToken()
            temp.left = self.Expr()
            if self.typToken != CALC_R_BRACKET:
                self.SendError(5)
            self.GetToken()
        else:
            temp = self.Expr4()
        return temp

    def Expr4(self):
        temp = None
        if self.typToken == CALC_NUMBER:
            temp = self.CreateNode(atof(self.curToken), None, None)
            self.GetToken()
        elif self.typToken == CALC_PI:
            temp = self.CreateNode(M_PI, None, None)
            self.GetToken()
        elif self.typToken == CALC_G:
            temp = self.CreateNode(F_G, None, None)
            self.GetToken()
        elif self.typToken == CALC_L_BRACKET:
            self.GetToken()
            temp = self.Expr()
            if self.typToken != CALC_R_BRACKET:
                self.SendError(5)
            self.GetToken()
        elif self.typToken == CALC_LEET:
            temp = self.CreateNode(H_LEET, None, None)
            self.GetToken()
        else:
            self.SendError(5)
        return temp

    def SendError(self, errNum):
        if self.curToken == TERMINATOR:
            print("Пустое выражение")
        elif errNum == 2:
            print("Внезапный конец выражения")
        elif (errNum == 3):
            print("Конец выражения ожидается")
        elif errNum == 4:
            print("Пропущеннаи открывающая скобка")
        elif errNum == 5:
            print("Пропущенна закрывающая скобка")
        else:
            print("Неизвестная ошибка")
        raise Exception('')

    def Compile(self, _expr):
        self.pos = 0
        self.expr = _expr + [TERMINATOR]
        if self.root != None:
            self.root = None
        self.GetToken()
        if self.typToken == CALC_END:
            self.SendError(2)
        self.root = self.Expr()
        if self.typToken != CALC_END:
            self.SendError(3)
        return True

    def GetResult(self):
        return self.result

    def Evaluate(self):
        self.result = self.CalcTree(self.root)

    def CalcTree(self, tree):
        temp = 0
        if tree.left == None and tree.right == None:
            return tree.value
        else:
            op = tree.value
            if op == OP_PLUS:
                return self.CalcTree(tree.left) + self.CalcTree(tree.right)
            elif op == OP_MINUS:
                return self.CalcTree(tree.left) - self.CalcTree(tree.right)
            elif op == OP_MULTIPLY:
                return self.CalcTree(tree.left) * self.CalcTree(tree.right)
            elif op == OP_DIVIDE:
                return self.CalcTree(tree.left) / self.CalcTree(tree.right)
            elif op == OP_PERCENT:
                return self.CalcTree(tree.left) % (self.CalcTree(tree.right))
            elif op == OP_POWER:
                return math.pow(self.CalcTree(tree.left), self.CalcTree(tree.right))
            elif op == OP_UMINUS:
                return -self.CalcTree(tree.left)
            elif op == OP_SIN:
                return math.sin(self.CalcTree(tree.left))
            elif op == OP_COS:
                return math.cos(self.CalcTree(tree.left))
            elif op == OP_TG:
                return math.tan(self.CalcTree(tree.left))
            elif op == OP_CTG:
                return 1.0 / math.tan(self.CalcTree(tree.left))
            elif op == OP_ARCSIN:
                return math.asin(self.CalcTree(tree.left))
            elif op == OP_ARCCOS:
                return math.acos(self.CalcTree(tree.left))
            elif op == OP_ARCTG:
                return math.atan(self.CalcTree(tree.left))
            elif op == OP_ARCCTG:
                return M_PI / 2.0 - math.atan(self.CalcTree(tree.left))
            elif op == OP_SH:
                temp = self.CalcTree(tree.left)
                return (math.exp(temp) - math.exp(-temp)) / 2.0
            elif op == OP_CH:
                temp = self.CalcTree(tree.left)
                return (math.exp(temp) + math.exp(-temp)) / 2.0
            elif op == OP_TH:
                temp = self.CalcTree(tree.left)
                return (math.exp(temp) - math.exp(-temp)) / (math.exp(temp) + math.exp(-temp))
            elif op == OP_CTH:
                temp = self.CalcTree(tree.left)
                return (math.exp(temp) + math.exp(-temp)) / (math.exp(temp) - math.exp(-temp))
            elif op == OP_EXP:
                return math.exp(self.CalcTree(tree.left))
            elif op == OP_LG:
                return math.log10(self.CalcTree(tree.left))
            elif op == OP_LN:
                return math.log(self.CalcTree(tree.left))
            elif op == OP_SQRT:
                return math.sqrt(self.CalcTree(tree.left))
            elif op == OP_IN:
                return 1
        return 0


if __name__ == "__main__":
    CALC = TCALC()

    print("Введите выражение: ")

    while True:
        try:
            CALC.Compile(list(str(input(">> "))))
            CALC.Evaluate()
            print("Ответ: ", CALC.GetResult())
            print("")
        except:
            break
