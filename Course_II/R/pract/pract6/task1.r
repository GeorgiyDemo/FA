'Аналогично примеру, разобранному выше, создать функцию, в к
оторой переданный параметр х возводится в степень y, а затем делится на параметр z.
Результат выводится на экран. В случае деления на ноль функция должна
выводить сообщение об ошибке в параметре z.
'

#Функция
calc <- function(x, y, z) {
  if ((typeof(x) != "double") ||
      (typeof(y) != "double") || (typeof(z) != "double"))  {
    print(
      "Предупреждение о несоответствии типов! Возможно вы передаете переменные некорректного типа!"
    )
  }
  
  if (y == 0) {
    z <- "Ошибка, деление на 0"
  } else{
    z <- (x ^ y) / z
  }
  return(z)
}

#Основная программа
{
  #Запускаем функцию нормально
  result <- calc(4, 6, 7)
  print(result)
  
  #Запускаем функцию с делением на 0
  result <- calc(4, 0, 7)
  print(result)
  
}