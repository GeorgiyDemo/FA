"
Изучить 5-7 любых функций языка R, исследовать передачу параметров в эти функции
Выяснить формальные имена параметров и значения параметров по умолчанию.
Проверить работу этих функций, написав для этого простейшие тестирующие программ.
По результатам проверки работы функций написать по каждой функции краткую справку
в виде комментария в тестирующей программе.
"
#В качестве параметра передается значение, которое необходимо вывести
print("Пример вывода")

vector <- c(5,54,6,3,5,54,645,754,654,6,54,34,32)
#в качестве аргумента предается вектор/сущность, которую можно посчитать
length(vector)

#добавляет элементы values в вектор x
vector <- append(vector,42)
length(vector)

# сумма элементов объекта
sum(vector)

# произведение элементов объекта
prod(vector)