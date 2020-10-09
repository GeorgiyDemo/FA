saleLevel <- sample(0:100, 10, replace = T)
all.in <- vector()
all.out <- vector()

#Заполняем поставки
for (i in (10:20)) {
  all.in <- c(all.in, round(runif(7) * 30 * i + 10 * i))
}

a <-
  c("Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье")
in.tab1 <- data.frame("День недели" = a, "Поставки" = c(all.in[1:7]))
in.tab2 <- data.frame("День недели" = a, "Поставки" = c(all.in[8:14]))
in.tab3 <- data.frame("День недели" = a, "Поставки" = c(all.in[15:21]))
in.tab4 <- data.frame("День недели" = a, "Поставки" = c(all.in[22:28]))
in.tab5 <- data.frame("День недели" = a, "Поставки" = c(all.in[29:35]))
in.tab6 <- data.frame("День недели" = a, "Поставки" = c(all.in[36:42]))
in.tab7 <- data.frame("День недели" = a, "Поставки" = c(all.in[43:49]))
in.tab8 <- data.frame("День недели" = a, "Поставки" = c(all.in[50:56]))
in.tab9 <- data.frame("День недели" = a, "Поставки" = c(all.in[57:63]))
in.tab10 <- data.frame("День недели" = a, "Поставки" = c(all.in[64:70]))

#Заполняем продажу с зависимостью от уровня поставок и поставок
for (i in (1:length(all.in))) {
  all.out <-
    append(all.out, round(all.in[i] * saleLevel[((i - 1) %/% 7)] / 100))
}

out.tab1 <- data.frame("День недели" = a, "Поставки" = c(all.out[1:7]))
out.tab2 <- data.frame("День недели" = a, "Поставки" = c(all.out[8:14]))
out.tab3 <- data.frame("День недели" = a, "Поставки" = c(all.out[15:21]))
out.tab4 <- data.frame("День недели" = a, "Поставки" = c(all.out[22:28]))
out.tab5 <- data.frame("День недели" = a, "Поставки" = c(all.out[29:35]))
out.tab6 <- data.frame("День недели" = a, "Поставки" = c(all.out[36:42]))
out.tab7 <- data.frame("День недели" = a, "Поставки" = c(all.out[43:49]))
out.tab8 <- data.frame("День недели" = a, "Поставки" = c(all.out[50:56]))
out.tab9 <- data.frame("День недели" = a, "Поставки" = c(all.out[57:63]))
out.tab10 <-
  data.frame("День недели" = a, "Поставки" = c(all.out[64:70]))

#Если продаем больше, чем покупаем, то это неправильно и исправаляем это недоразумение
if (sum(in.tab1[, 2]) < sum(out.tab1[, 2])) {
  t <- out.tab1[, 2]
  out.tab1[, 2] <- in.tab1[, 2]
  in.tab1 <- t
}

#Закидываем все значения in в вектор
in.tabl <-
  c(
    in.tab1,
    in.tab2,
    in.tab3,
    in.tab4,
    in.tab5,
    in.tab6,
    in.tab7,
    in.tab8,
    in.tab9,
    in.tab10
  )
#Закидываем все значения out в вектор
out.tabl <-
  c(
    out.tab1,
    out.tab2,
    out.tab3,
    out.tab4,
    out.tab5,
    out.tab6,
    out.tab7,
    out.tab8,
    out.tab9,
    out.tab10
  )

for (i in (1:10)) {
  write.table(
    in.tabl[c(i * 2 - 1, i * 2)],
    file = paste(
      '/Users/georgiydemo/Projects/FA/Course II/R/Diksi/shop',
      as.character(i),
      '/in.txt',
      sep = ''
    ),
    col.names = TRUE,
    row.names = FALSE,
    sep = ' ',
    dec = ','
  )
  write.table(
    out.tabl[c(i * 2 - 1, i * 2)],
    file = paste(
      '/Users/georgiydemo/Projects/FA/Course II/R/Diksi/shop',
      as.character(i),
      '/out.txt',
      sep = ''
    ),
    col.names = TRUE,
    row.names = FALSE,
    sep = ' ',
    dec = ','
  )
}
