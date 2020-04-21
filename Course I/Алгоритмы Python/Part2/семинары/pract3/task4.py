"""
4*.  Дано слово, состоящее только из строчных латинских букв. Проверьте, является ли это
слово палиндромом. Выведите YES или NO. При решении этой задачи нельзя пользоваться
циклами и нельзя использовать срезы с шагом, отличным от 1
Пример: radar YES
Yes No
"""


def r_palindrome(str_input):
    if len(str_input) == 1:
        return "YES"
    else:
        if str_input[:1] == str_input[-1:]:
            if len(str_input) == 2:
                return "YES"
            return r_palindrome(str_input[1:-1])
        return "NO"


if __name__ == "__main__":
    str_input = input("Введите слово для проверки на палиндром -> ")  # лимузинизумил
    print(r_palindrome(str_input))
