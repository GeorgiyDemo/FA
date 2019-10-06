from random import randint
MATRIX_WEIGHT, MATRIX_HEIGHT = 8, 8

def createMatrix():
    m = [[randint(0, 4) for j in range(MATRIX_WEIGHT)] for i in range(MATRIX_HEIGHT)]
    return m
  
def printMatrix (matrix): 
   text = ' ' 
   for i in range (len(matrix)):
      print(i+1, end = "") 
      for j in range (len(matrix[i])):
          if matrix[i][j] == 1:
              text = '*'
          else:
              text = ' '
          print (" {} ".format(text), end = "" ) 
      print ()                 

def checkInstance(matrix):
    temp = 0
    for n in range(8):
        for j in range(8):
            if matrix[n][j] == 0 or matrix[n][j] == 2 or matrix[n][j] == 3 or matrix[n][j] == 4:
                temp += 1
    if temp == 64:
        return True
    else:
        return False   

def goMove(matrix, move):
    try:
        if move == 'a': inter = 0
        if move == 'b': inter = 1
        if move == 'c': inter = 2
        if move == 'd': inter = 3
        if move == 'e': inter = 4
        if move == 'f': inter = 5
        if move == 'g': inter = 6
        if move == 'h': inter = 7         
        elif move.isdigit(): 
            inter = int(move) -1
            for l in range(8):
                matrix[inter][l] = 0
            return matrix                        
        for l in range(8):
            matrix[l][inter] = 0           
        return matrix
    except Exception:
        return False    

matrix = createMatrix()      
print("---------------\nИгровое поле сгенерировано:\n")
print("  a  b  c  d  e  f  g  h")      
printMatrix(matrix)
checkInstance(matrix)
turn = 1

while not checkInstance(matrix):
    if turn == 1:
        print("------------------------\nХодит Игрок I\nВведите строку или столбец, чтобы сделать ход.\n------------------------")
        move = input("Ввод: ")
        if not goMove(matrix, move):
            print("Некорректный ввод. Сделайте ход заного:")
            turn = 1
            print(" 'a  b  c  d  e  f  g  h")    
            printMatrix(matrix)
        else:    
            matrix = goMove(matrix, move)
            if checkInstance(matrix):
                print("Игра окончена, победил игрок I")
            else:    
                print(" 'a  b  c  d  e  f  g  h")   
                printMatrix(matrix)            
            turn = 2    
    elif turn == 2:
        print("------------------------\nХодит Игрок II\nВведите строку или столбец, чтобы сделать ход.\n------------------------")
        move = input("Ввод: ")
        if not goMove(matrix, move):
            print("Некорректный ввод. Сделайте ход заного:")
            turn = 2
            print(" 'a  b  c  d  e  f  g  h")    
            printMatrix(matrix)
        else:    
            matrix = goMove(matrix, move)
            if checkInstance(matrix):
                print()
                print("Игра окончена, победил игрок II")
            else:
                print(" 'a  b  c  d  e  f  g  h")   
                printMatrix(matrix)
            turn = 1    
