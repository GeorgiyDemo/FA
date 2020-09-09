"
Создать десять переменных разных типов, проверить их тип с помощью функции typeof().
Проверить с помощью этой функции типы следующих констант
29, 23i, -34L, 2/3, 4/2, 0xA, 0XbL – 120L, 0XbL – 120, 0XbL * 17.
Объяснить полученные результаты.
"

#Десять переменных
print("Вывод 10 переменных разных типов")
a <- "String"
typeof(a)
b <- 1.2
typeof(b)
c1 <- c(1,2,5.3,6,-2,4)
typeof(c1)
d <- 10i
typeof(d)
e <- matrix(1:20, nrow=5,ncol=4)
typeof(e)
f <- list(name="Fred", age=5.3)
typeof(f)
g <- c(rep("male",20), rep("female", 30))
g <- factor(g)
typeof(g)
h = FALSE
print(h)
i = 0xAb
typeof(i)

#Вывод констант и их типов
print("Вывод констант и их типов")
localelist <- list(29, 23i, -34L, 2/3, 4/2, 0xA, 0XbL - 120L, 0XbL - 120, 0XbL * 17.)
for (element in localelist) {
  print(element)
  print(typeof(element))
}


