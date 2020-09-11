"
Написать формулу получения 10 случайных целых чисел из диапазона (min = -7, max = 28
с помощью функции runif(),
не используя при ее вызове задания минимального и максимального значений.
"
w <- runif(10000)
w <- round(w, digits = 2)
w <- w * 100
result=c()
for (number in w)
  if (number >= -7 & number <= 28)
    result <- append(result, number)
print(sample(result,10))

