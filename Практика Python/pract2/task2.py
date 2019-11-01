"""
Задача 2.
Задание:
Реализовать текстовый калькулятор для решения системы уравнений. Возможные уравнения
внутри системы: линейное, квадратное, кубическое, биквадратное. Добавить в программу
считывание с файла системы уравнения. Программа должна автоматически определять вид
уравнения, без явных указателей. Принцип ввода реализовать на усмотрение разработчика,
добавить его рядом с программой в виде текстового документа. Встроенными функциями и
библиотечными для решения уравнений и систем пользоваться ЗАПРЕЩЕНО.
//eval юзать также нельзя

To build an expressional calculator, you need to go through these steps :

1) Segmentate the expression into a list of tokens
2) Parse the tokens into recognizable lexemes( numbers, operator, etc)
3) Transform the list into a tree structure based on the order of operations
4) Calculate the result of top root, which requires the results from its branch(es)

Какие-то мысли:
Если у нас перед переменной стоит оператор умножения, значит есть коэффицент. Смотрим наши переменные в линейном уравнении
ах+ву+с=0
Если у нас перед первой переменной нет умножения, значит ее выражаем, оставляем только ее и переносим за равно все остальное
с противоположными знаками
Если у нас перед перед первой переменной есть знак умножения, смотрим на вторую
если перед ней нет знака умножения, то делаем то же самое
Если обе переменные с коэффицентами, то смотрим, какой коэффицент меньше
выражаем переменную с таким коэффицентом: переносим эту переносим все за равно и делим на этот коэффицент

Допустим, мы выразили х
когда мы выразили, мы должны пройтись по уравнениям и запрашивать, есть ли там х
Если есть, то заменять , если нет, то идти дальше
"""

import re
TXT_FILE = "input.txt"

class GetValues():
    def __init__(self):
        self.file2text()
    def file2text(self):
        with open(TXT_FILE, 'r') as stream:
            list_m = stream.readlines()
            self.text = [e.replace("\n", "") for e in list_m]

class ProcessingValuesClass():
    def __init__(self, input_list):
        self.list_input = input_list
        self.processing()
    
    def processing(self):
        list_input = self.list_input
        for expression in list_input:
            self.solver(expression)
    
    def get_numbers(self):
        expression = self.expression
        digists = re.findall(r'\d+', expression)
        print(digists)
        for digist in digists:
            indices = [i for i, x in enumerate(expression) if x == digist]
            for index in indices:
                self.dictionary[index] = "NUMBER"

    def get_vars(self):
        expression = self.expression
        chars = re.findall(r'[a-zA-Z]+', expression)
        for char in chars:
            indices = [i for i, x in enumerate(expression) if x == char]
            for index in indices:
                self.dictionary[index] = "VAR"

    def get_operations(self):
        expression = self.expression
        operation_list = ["*","/","-","+"]
        for i in range(len(expression)):
            if expression[i] in operation_list:
                self.dictionary[i] = "OPERATION"
            elif expression[i] == "=":
                self.dictionary[i] = "EQUALLY"
            elif expression[i] ==  "^":  
                self.dictionary[i] = "POWER"  

    def solver(self, expression):
        
        self.dictionary = {}
        self.expression = expression
        for i in range(len(expression)):
            self.dictionary[i]=None
        
        self.get_numbers()
        self.get_vars()
        self.get_operations()

        print(self.dictionary)
        #{0: 'NUMBER', 1: 'OPERATION', 2: 'VAR', 3: 'POWER', 4: 'NUMBER', 5: 'OPERATION', 6: 'NUMBER', 7: 'OPERATION', 8: 'VAR', 9: 'OPERATION', 10: 'VAR', 11: 'EQUALLY', 12: 'OPERATION', 13: 'NUMBER'}

if __name__ == "__main__":
    o = GetValues()
    process_obj = ProcessingValuesClass(o.text)