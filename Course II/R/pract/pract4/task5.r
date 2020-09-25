'
Создать несколько векторов разных типов и длины и написать
с ними три формулы с использованием логических операций.
Объяснить полученный результат, добавив в скрипт комментарии
'

vector1 <- c("string1", "string2", "string3")
vector2 <- c(1,26,4,4,76,43)
vector3 <- c(TRUE, FALSE, TRUE)
vector4 <- c(3i, 53.4i, 4i)

result1 <- vector2 & vector3
result1 <- vector2 && vector3
result3 <- vector2 | vector4
result4 <- vector3 || vector4


#Будет ошибка
result2 <- vector1 & vector2