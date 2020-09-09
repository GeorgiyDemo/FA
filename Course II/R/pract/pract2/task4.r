"
Исследовать правила неявного преобразования типов, выполнив примеры, аналогичные примерам из п.8.
Определить правила преобразования для переменных следующих типов:
integer и double
integer и logical
logical и character
double и logical
double и character
По результатам исследования сформулировать общее правило преобразования типов в R.
"

result <- 1 + 1.3
typeof(result)

result <- 1 + TRUE
typeof(result)

result <- TRUE + "MEOW"
typeof(result)
