class UtilClass:
    """Класс со всякой фигней"""
    @staticmethod
    def xint2char(xint):
        """Конвертирование числа в букву"""
        d = {0:"A",1:"B", 2:"C", 3:"D", 4:"E", 5: "F", 6: "G", 7: "H"}
        
        if xint in d:
            return d[xint]
        else:
            raise ValueError("Нет ключа для полученного xint {}".format(xint))
     
    @staticmethod
    def char2xint(char):
        """Конвертирование буквы в число"""
        d = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E":4, "F":5, "G":6 , "H":7,
            "a": 0, "b" : 1, "c" :2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
        }
        if char in d:
            return d[char]
        else:
            raise ValueError("Нет ключа для полученного char {}".format(char))
    
    @staticmethod
    def checkxy_value(part):
        """Проверка на корректные на координаты xy"""
        if type(part) != str or len(part) != 2:
            return False

        l1 = ["A", "B", "C", "D", "E", "F", "G", "H", "a","b", "c", "d", "e", "f", "g", "h"]
        l2 = list(map(str, range(1,9)))
        if part[0] in l1 and part[1] in l2:
            return True
        return False