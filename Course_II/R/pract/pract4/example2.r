w1 <- c(3,4,4,5)
print(typeof(w1))
w2 <- c(4, 1)
print(typeof(w2))
w3 <- w1 + w2
print(w3)

x <- c(1, 0, 0, 2) # вектор x
y <- c(0, 1, 1, 2) # вектор y
z <- x + y # прибавляем к каждому элементу x элемент y
print(z)

w3 <- c(Inf, NULL, NA, FALSE, 18, NaN)
print(typeof(w3))
w4 <- c(Inf, NULL, NA, FALSE, 18L, NaN)
print(typeof(w4))
w5 <- c(Inf, NULL, NA, FALSE, '18', NaN)
print(typeof(w5))
w6 <- c(NULL)
print(typeof(w6))

#Если требуется вектор-заготовка для хранения данных определенного типа и определенного размера,
#вызывают функцию vector() с заданием нужных параметров:
z <- vector()
z2 <- vector(mode='numeric', length=129)
z3 <- vector(mode='logical', length=22)
z4 <- vector(mode='integer', length=34)
z5 <- vector(mode='character', length=0)
z6 <- vector(mode='double', length=19)


z6 <- vector(length=19, mode='double')
z7 <-vector(length=19) # тип данных задается по умолчанию
z8 <- vector(mode='double') # длина вектора задается по умолчанию

z2 <- numeric(length=129)
z3 <- logical(length=22)
z4 <- integer(length=34)
z5 <- character(length=0)

w <- c(10:3)
w <- c(1:20, 3)
w <- c(10:5, 5:10, 15:18)


w <- rep(с(0, -1, 1:3), times = 3)
print(w)
w <- rep(с(0, -1, 1:3), each = 3)
print(w)
w <- rep(с(0, -1, 1:3), each = 3, times = 2)
print(w)


w <- seq(4, from=12, length.out = 10)
print(w)

#Задание.
#Приведите пример создания вектора через вызов функции seq() в случае одновременного использования параметров by и length.out. Объясните правило формирования вектора в этом случае.
w <- seq(from = -40, by = 3.5, length.out = 50)
print(w)

#Самостоятельно исследуйте параметры и поведение seq_len() и объясните
# в каком случае вызов seq() приведет к вызову и исполнению seq_len().
w1 <- seq_len(100)
print(w1)

w2 <- seq(from = 0, by = 0.5, length.out = 20)
print(w2)

min(w2)
max(w2)


