'
Аналогично заданию 2, проверить работу арифметических операторов для векторов. Последовательно использовать векторы:
1) одного типа, одного размера
2) одного типа, разных размеров
3) разных типов, одного размера
4) разных типов, разного размера
Обобщить результаты расчетов в виде правил вычисления результирующего вектора.
'

#Одного типа, одного размера
vector1 <- c(1,2,3,4)
vector2 <- c(4,6,3,6)
vector1 + vector2
vector1 - vector2
vector1 * vector2
vector1 / vector2


#Одного типа, разных размеров
vector1 <- c(1,2,3,4, 4,5,2)
vector2 <- c(4,6,3,6)
vector1 + vector2
vector1 - vector2
vector1 * vector2
vector1 / vector2

#Разных типов, одного размера
vector1 <- c(TRUE, FALSE, TRUE, TRUE)
vector2 <- c(4,6,3,6)
vector1 + vector2
vector1 - vector2
vector1 * vector2
vector1 / vector2

#Разных типов, разного размера
vector1 <- c(TRUE, FALSE, TRUE, TRUE)
vector2 <- c(4,6,3,6,6,2,6,2,5)
vector1 + vector2
vector1 - vector2
vector1 * vector2
vector1 / vector2
