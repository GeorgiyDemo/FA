#Функция
calc <- function(number,
                 parameter = "rus",
                 short = FALSE) {
  #Округление
  number <- round(number, 0)
  
  #Если больше - берем остаток
  if (number > 12) {
    number <- number %% 12
  }
  #Если меньше 1 - пробел
  if (number < 1) {
    return(" ")
  }
  
  #Если есть английский - выводим на англе
  if (is.element(parameter,
                 c("Eng", "eng", "English", "english", "англ", "Англ", "анг"))) {
    if (short) {
      day <- switch (
        number,
        "Jan.",
        "Feb.",
        "Mar.",
        "Apr.",
        "May.",
        "Jun.",
        "Jul.",
        "Aug.",
        "Sep.",
        "Oct.",
        "Nov.",
        "Dec."
      )
    } else {
      day <- switch (
        number,
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      )
    }
    #Если нет английского -выводим на русском
  } else{
    if (short) {
      day <- switch (
        number,
        "Янв.",
        "Фев.",
        "Мрт,",
        "Апр.",
        "Май.",
        "Июн.",
        "Июл.",
        "Авг.",
        "Сен.",
        "Окт.",
        "Ноя.",
        "Дек."
      )
    } else {
      day <- switch (
        number,
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь"
      )
    }
  }
  #Отдаем значение
  return(day)
}

#Основная программа
{
  #Запускаем функцию нормально
  result <- calc(12)
  print(result)
  
  result <- calc(13, "Eng", TRUE)
  print(result)
}