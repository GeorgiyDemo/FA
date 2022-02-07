"
Используя цикл, с клавиатуры ввести 8 чисел. Расположить их по
убыванию. Результат вывести в виде строки типа «27 > 12 > 5 > -2 ...»
"
{
  all_values = c()
  numbers_count = 8
  
  for (var in 1:numbers_count)
  {
    N <- as.integer(readline("Введите число -> "))
    all_values <- append(all_values, N)
  }
  
  all_values <- sort(all_values, decreasing = FALSE)
  
  out_string = c()
  for (value in rev(all_values)) {
    out_string <- append(out_string, value)
    out_string <- append(out_string, ">")
  }
  
  
  out_string <- out_string[1:(length(out_string) - 1)]
  print(paste(out_string))
  
}
