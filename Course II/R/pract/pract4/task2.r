"
a<- с(7:4, 0)
b<-с(8, 10.5, 0, -2, 9)
Написать программу, выполняющую следующие действия над векторами:
1) Сложение векторов a + b
2) Умножение векторов a * b
3) Деление векторов a / b
4) Нахождение среднего арифметического для каждого вектора
5) Нахождение суммы элементов каждого вектора
6) Представление результатов расчетов на экране
Указание. В программах использовать функции print(), paste(), paste0(), sum(), mean().
"

a <- c(7:4, 0)
print("Вектор А")
print(a)

b <- c(8, 10.5, 0, -2, 9)
print("Вектор B")
print(b)

result1 <- a + b
print(result1)

result2 <- a * b
print(result2)

result3 <- a / b
print(result3)

#Сред арифметическое
print(paste("Сред арифметическое А =",mean(a)))
print(paste("Сред арифметическое B =",mean(b)))

#Сумма элементов каждого вектора
print(paste0("Сумма элементов А=", sum(a)))
print(paste0("Сумма элементов B=", sum(b)))




