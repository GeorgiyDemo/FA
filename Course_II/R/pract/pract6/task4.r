#Функция
calc <- function(number,
                 parameter = "rus",
                 short = FALSE) {
  #Округление
  number <- round(number, 0)
  
  #Если больше - берем остаток
  if (number > 7) {
    number <- number %% 7
  }
  #Если меньше 1 - пробел
  if (number < 1) {
    return(" ")
  }
  
  #Если есть английский - выводим на англе
  if (is.element(parameter,
                 c("Eng", "eng", "English", "english", "англ", "Англ", "анг"))) {
    if (short) {
      day <- switch (number,
                     "Mon.",
                     "Tue.",
                     "Wed.",
                     "Thu.",
                     "Fri.",
                     "Sat.",
                     "Sun.")
    } else {
      day <- switch (
        number,
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
      )
    }
    #Если нет английского -выводим на русском
  } else{
    if (short) {
      day <- switch (number,
                     "Пон..",
                     "Втр.",
                     "Сред.",
                     "Чет.",
                     "Пят.",
                     "Суб.",
                     "Вос.")
    } else {
      day <- switch (
        number,
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
      )
    }
  }
  #Отдаем значение
  return(day)
}

#Основная программа
{
  #Запускаем функцию нормально
  result <- calc(20)
  print(result)
  
  result <- calc(20, "Eng", TRUE)
  print(result)
}