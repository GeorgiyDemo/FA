"
Требовать от Пользователя ввод чисел до тех пор, пока он не наберет слово «Стоп»
в любом регистре, в любом сочетании заглавных и прописных букв.
Использовать функцию toupper() или tolower().
"
{
  exitflag <- FALSE
  thisword <- "Стоп"
  
  while (exitflag == FALSE)
  {
    user_input <- toupper(readline("Введите данные -> "))
    if (user_input == toupper(thisword)){
      exitflag <- TRUE
      print("Пользователь ввел стоп-слово")
    }
  }
}