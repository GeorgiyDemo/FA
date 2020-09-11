"
Написать формулу получения 20 случайных действительных чисел из диапазо
а (min = -7, max = -2) с помощью функции sample(),
не используя при ее вызове задания минимального и максимального значений.
"
w <- sample(10000)
w <- w * -0.1000
result=c()
for (number in w)
  if (number >= -7 & number <= -2)
    result <- append(result, number)
result <- sample(result,20)
print(result)
