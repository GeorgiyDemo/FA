#install.packages('rJava', type='mac.binary')
#install.packages('xlsx', type='mac.binary')
library("xlsx")

#Устанавливаем директорию
getwd()
setwd("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/analytics")
dir()

#Ввод входных данных
in1 <- read.table(file = "store1_in.txt", head = TRUE)
in2 <- read.table(file = "store2_in.txt", head = TRUE)
in3 <- read.table(file = "store3_in.txt", head = TRUE)
in4 <- read.table(file = "store4_in.txt", head = TRUE)
in5 <- read.table(file = "store5_in.txt", head = TRUE)
in6 <- read.table(file = "store6_in.txt", head = TRUE)
in7 <- read.table(file = "store7_in.txt", head = TRUE)
in8 <- read.table(file = "store8_in.txt", head = TRUE)
in9 <- read.table(file = "store9_in.txt", head = TRUE)
in10 <- read.table(file = "store10_in.txt", head = TRUE)

#Ввод выходных данных
out1 <- read.table(file = "store1_out.txt", head = TRUE)
out2 <- read.table(file = "store2_out.txt", head = TRUE)
out3 <- read.table(file = "store3_out.txt", head = TRUE)
out4 <- read.table(file = "store4_out.txt", head = TRUE)
out5 <- read.table(file = "store5_out.txt", head = TRUE)
out6 <- read.table(file = "store6_out.txt", head = TRUE)
out7 <- read.table(file = "store7_out.txt", head = TRUE)
out8 <- read.table(file = "store8_out.txt", head = TRUE)
out9 <- read.table(file = "store9_out.txt", head = TRUE)
out10 <- read.table(file = "store10_out.txt", head = TRUE)

#Параметры
P <- 8000
P_supply <- 5500
P_until <-  400
rev <- rep(0, 12)
profit <- rep(0, length(rev))

#Столбец B с названиями
res.tab <-
  data.frame(
    " " = c(
      "Магазин 1",
      "Магазин 2",
      "Магазин 3",
      "Магазин 4",
      "Магазин 5",
      "Магазин 6",
      "Магазин 7",
      "Магазин 8",
      "Магазин 9",
      "Магазин 10",
      "Итого",
      "Среднее"
    ),
    "Выручка" = rev,
    "Прибыль" = profit
  )
sale <- rep(0, nrow(res.tab))
res.tab$Реализация  <- sale
res.tab["Реализация"] <- sale
res.tab$"Списание, конт." <- 0
res.tab$"Равномерность продаж" <- 0
res.tab$"Продажи макс" <- 0
День  <- rep(0, 12)
res.tab <- cbind(res.tab,  День)
res.tab$"Продажи мин" <- 0
День  <- rep(0, 12)
res.tab <- cbind(res.tab,  День)
res.tab$"Списание макс" <- 0
День  <- rep(0, 12)
res.tab <- cbind(res.tab,  День)
res.tab[c(11:12), c(7:12)] <- ""
colnames(res.tab)[6] <- "sd"

# Списание за неделю
res.tab[1, 5] <- sum(in1[, 2]) - sum(out1[, 2])
res.tab[2, 5] <- sum(in2[, 2]) - sum(out2[, 2])
res.tab[3, 5] <- sum(in3[, 2]) - sum(out3[, 2])
res.tab[4, 5] <- sum(in4[, 2]) - sum(out4[, 2])
res.tab[5, 5] <- sum(in5[, 2]) - sum(out5[, 2])
res.tab[6, 5] <- sum(in6[, 2]) - sum(out6[, 2])
res.tab[7, 5] <- sum(in7[, 2]) - sum(out7[, 2])
res.tab[8, 5] <- sum(in8[, 2]) - sum(out8[, 2])
res.tab[9, 5] <- sum(in9[, 2]) - sum(out9[, 2])
res.tab[10, 5] <- sum(in10[, 2]) - sum(out10[, 2])
res.tab[11, 5] <- sum(res.tab[1:10, 5])
res.tab[12, 5] <- mean(res.tab[1:10, 5])

# Продажи максимальные
res.tab[1, 7] <- max(out1[, 2])
res.tab[1, 8] <- out1[which.max(out1[, 2]), 1]
res.tab[2, 7] <- max(out2[, 2])
res.tab[2, 8] <- out2[which.max(out2[, 2]), 1]
res.tab[3, 7] <- max(out3[, 2])
res.tab[3, 8] <- out3[which.max(out3[, 2]), 1]
res.tab[4, 7] <- max(out4[, 2])
res.tab[4, 8] <- out4[which.max(out4[, 2]), 1]
res.tab[5, 7] <- max(out5[, 2])
res.tab[5, 8] <- out5[which.max(out5[, 2]), 1]
res.tab[6, 7] <- max(out6[, 2])
res.tab[6, 8] <- out6[which.max(out6[, 2]), 1]
res.tab[7, 7] <- max(out7[, 2])
res.tab[7, 8] <- out7[which.max(out7[, 2]), 1]
res.tab[8, 7] <- max(out8[, 2])
res.tab[8, 8] <- out8[which.max(out8[, 2]), 1]
res.tab[9, 7] <- max(out9[, 2])
res.tab[9, 8] <- out9[which.max(out9[, 2]), 1]
res.tab[10, 7] <- max(in10[, 2])
res.tab[10, 8] <- out1[which.max(in10[, 2]), 1]

# Продажи минимальные
res.tab[1, 9] <- min(out1[, 2])
res.tab[1, 10] <- out1[which.min(out1[, 2]), 1]
res.tab[2, 9] <- min(out2[, 2])
res.tab[2, 10] <- out2[which.min(out2[, 2]), 1]
res.tab[3, 9] <- min(out3[, 2])
res.tab[3, 10] <- out3[which.min(out3[, 2]), 1]
res.tab[4, 9] <- min(out4[, 2])
res.tab[4, 10] <- out4[which.min(out4[, 2]), 1]
res.tab[5, 9] <- min(out5[, 2])
res.tab[5, 10] <- out5[which.min(out5[, 2]), 1]
res.tab[6, 9] <- min(out6[, 2])
res.tab[6, 10] <- out6[which.min(out6[, 2]), 1]
res.tab[7, 9] <- min(out7[, 2])
res.tab[7, 10] <- out7[which.min(out7[, 2]), 1]
res.tab[8, 9] <- min(out8[, 2])
res.tab[8, 10] <- out8[which.min(out8[, 2]), 1]
res.tab[9, 9] <- min(out9[, 2])
res.tab[9, 10] <- out9[which.min(out9[, 2]), 1]
res.tab[10, 9] <- min(out10[, 2])
res.tab[10, 10] <- out10[which.min(out10[, 2]), 1]

# Списание максимальное
res.tab[1, 11] <- max(c(in1[, 2] - out1[, 2]))
res.tab[2, 11] <- max(c(in2[, 2] - out2[, 2]))
res.tab[3, 11] <- max(c(in3[, 2] - out3[, 2]))
res.tab[4, 11] <- max(c(in4[, 2] - out4[, 2]))
res.tab[5, 11] <- max(c(in5[, 2] - out5[, 2]))
res.tab[6, 11] <- max(c(in6[, 2] - out6[, 2]))
res.tab[7, 11] <- max(c(in7[, 2] - out7[, 2]))
res.tab[8, 11] <- max(c(in8[, 2] - out8[, 2]))
res.tab[9, 11] <- max(c(in9[, 2] - out9[, 2]))
res.tab[10, 11] <- max(c(in10[, 2] - out10[, 2]))
res.tab[1, 12] <- in1[which.max(c(in1[, 2] - out1[, 2])), 1]
res.tab[2, 12] <- in2[which.max(c(in2[, 2] - out2[, 2])), 1]
res.tab[3, 12] <- in3[which.max(c(in3[, 2] - out3[, 2])), 1]
res.tab[4, 12] <- in4[which.max(c(in4[, 2] - out4[, 2])), 1]
res.tab[5, 12] <- in5[which.max(c(in5[, 2] - out5[, 2])), 1]
res.tab[6, 12] <- in6[which.max(c(in6[, 2] - out6[, 2])), 1]
res.tab[7, 12] <- in7[which.max(c(in7[, 2] - out7[, 2])), 1]
res.tab[8, 12] <- in8[which.max(c(in8[, 2] - out8[, 2])), 1]
res.tab[9, 12] <- in9[which.max(c(in9[, 2] - out9[, 2])), 1]
res.tab[10, 12] <- in10[which.max(c(in10[, 2] - out10[, 2])), 1]

# Реализация за неделю
res.tab[1, 4] <- sum(out1[, 2])
res.tab[2, 4] <- sum(out2[, 2])
res.tab[3, 4] <- sum(out3[, 2])
res.tab[4, 4] <- sum(out4[, 2])
res.tab[5, 4] <- sum(out5[, 2])
res.tab[6, 4] <- sum(out6[, 2])
res.tab[7, 4] <- sum(out7[, 2])
res.tab[8, 4] <- sum(out8[, 2])
res.tab[9, 4] <- sum(out9[, 2])
res.tab[10, 4] <- sum(out10[, 2])
res.tab[11, 4] <- sum(res.tab[1:10, 4])
res.tab[12, 4] <- mean(res.tab[1:10, 4])

# Выручка
res.tab[1, 2] <- P * res.tab[1, 4]
res.tab[2, 2] <- P * res.tab[2, 4]
res.tab[3, 2] <- P * res.tab[3, 4]
res.tab[4, 2] <- P * res.tab[4, 4]
res.tab[5, 2] <- P * res.tab[5, 4]
res.tab[6, 2] <- P * res.tab[6, 4]
res.tab[7, 2] <- P * res.tab[7, 4]
res.tab[8, 2] <- P * res.tab[8, 4]
res.tab[9, 2] <- P * res.tab[9, 4]
res.tab[10, 2] <- P * res.tab[10, 4]
res.tab[11, 2] <- sum(res.tab[1:10, 2])
res.tab[12, 2] <- mean(res.tab[1:10, 2])

# Затраты
TC1 <- (sum(in1[, 2]) * P_supply) + (res.tab[1, 5] * P_until)
TC2 <- (sum(in2[, 2]) * P_supply) + (res.tab[2, 5] * P_until)
TC3 <- (sum(in3[, 2]) * P_supply) + (res.tab[3, 5] * P_until)
TC4 <- (sum(in4[, 2]) * P_supply) + (res.tab[4, 5] * P_until)
TC5 <- (sum(in5[, 2]) * P_supply) + (res.tab[5, 5] * P_until)
TC6 <- (sum(in6[, 2]) * P_supply) + (res.tab[6, 5] * P_until)
TC7 <- (sum(in7[, 2]) * P_supply) + (res.tab[7, 5] * P_until)
TC8 <- (sum(in8[, 2]) * P_supply) + (res.tab[8, 5] * P_until)
TC9 <- (sum(in9[, 2]) * P_supply) + (res.tab[9, 5] * P_until)
TC10 <- (sum(in10[, 2]) * P_supply) + (res.tab[10, 5] * P_until)

# Прибыль
res.tab[1, 3] <- res.tab[1, 2] - TC1
res.tab[2, 3] <- res.tab[2, 2] - TC2
res.tab[3, 3] <- res.tab[3, 2] - TC3
res.tab[4, 3] <- res.tab[4, 2] - TC4
res.tab[5, 3] <- res.tab[5, 2] - TC5
res.tab[6, 3] <- res.tab[6, 2] - TC6
res.tab[7, 3] <- res.tab[7, 2] - TC7
res.tab[8, 3] <- res.tab[8, 2] - TC8
res.tab[9, 3] <- res.tab[9, 2] - TC9
res.tab[10, 3] <- res.tab[10, 2] - TC10
res.tab[11, 3] <- sum(res.tab[1:10, 3])
res.tab[12, 3] <- mean(res.tab[1:10, 3])

# Равномерность
res.tab[1, 6] <- sd(out1[, 2])
res.tab[2, 6] <- sd(out2[, 2])
res.tab[3, 6] <- sd(out3[, 2])
res.tab[4, 6] <- sd(out4[, 2])
res.tab[5, 6] <- sd(out5[, 2])
res.tab[6, 6] <- sd(out6[, 2])
res.tab[7, 6] <- sd(out7[, 2])
res.tab[8, 6] <- sd(out8[, 2])
res.tab[9, 6] <- sd(out9[, 2])
res.tab[10, 6] <- sd(out10[, 2])
res.tab[11, 6] <- sum(res.tab[1:10, 6])
res.tab[12, 6] <- mean(res.tab[1:10, 6])

# Запись в .csv
write.table(
  res.tab,
  file = '/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица.csv',
  col.names = TRUE,
  row.names = FALSE,
  sep = ';',
  dec = ',',
  fileEncoding = 'UTF-8'
)

# Запись в .xlsx (это чтоб на маке отображалось корректно)
write.xlsx(res.tab,
           file = "/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица.xlsx",
           sheetName = "DATA",
           append = FALSE)