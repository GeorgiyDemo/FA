"
Написать формулу получения 10 случайных целых чисел из диапазона (min = -7, max = 28
с помощью функции runif(),
не используя при ее вызове задания минимального и максимального значений.
"
{
checker <- function(n,min,max){
  return(floor((runif(n) * ((max - min) + 1)) + min))
}

n <- 10
min <- -7
max <- 28
print(checker(n,min,max))

}