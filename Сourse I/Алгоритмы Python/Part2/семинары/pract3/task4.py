"""
4*.  Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это
слово палиндромом. Выведите YES или NO. При решении этой задачи нельзя пользоваться
циклами и нельзя использовать срезы с шагом, отличным от 1
Пример: radar YES
Yes No
"""

def r_palindrome(s):
    if len(s) == 1:
        return "YES"
    else:
        if s[:1] == s[-1:]:
            if len(s) == 2:
                return "YES"
            return r_palindrome(s[1:-1])
        return "NO" 

if __name__ == "__main__":
    print(r_palindrome("лимузинизумил"))