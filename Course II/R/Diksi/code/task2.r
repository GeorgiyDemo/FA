#install.packages('rJava', type='mac.binary')
#install.packages('xlsx', type='mac.binary')
library("xlsx")

#Цена продукта, который мы продаём
PRODUCT_PRICE = 500
#Устанавливаем директорию
setwd("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/analytics")

#Названия магазинов
shop_names <- c()
#Выручка
shop_revenues <- rep(0, 10)
#Прибыль
shop_profits <- rep(0, 10)
#Реализация
shop_sales <- c()
#Списание
shop_writeoffs <- c()
#Равномерность продаж
shop_sr <- rep(0, 10)
#Продажи макс
shop_sales_max <- rep(0, 10)
#День продажи макс
shop_sales_maxdays <- rep(0, 10)
#Продажи мин
shop_sales_min <- rep(0, 10)
#День продажи мин
shop_sales_mindays <- rep(0, 10)
#Списание макс
shop_writeoff_max <- rep(0, 10)
#День списания макс 
shop_writeoff_maxdays <- rep(0, 10)


for (i in 1:10){
  in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
  out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)
  
  #Название магазина
  shop_names <- append(shop_names, paste0('store',as.character(i)))
  
  #TODO Прибыль
  
  #Реализация
  shop_sales <- append(shop_sales, sum(out1[, 2]))
  
  #Списание
  shop_writeoffs <- append(shop_writeoffs, sum(in1[, 2]) - sum(out1[, 2]))
}

print(shop_names)

#Формируем датафрейм
table <- data.frame(shop_names,shop_revenues,shop_profits,shop_sales ,shop_writeoffs,shop_sr,shop_sales_max,shop_sales_maxdays,shop_sales_min,shop_sales_mindays,shop_writeoff_max,shop_writeoff_maxdays)

#Проставляем заголовки
col_headings <- c("Магазин" ,"Выручка (руб)" ,"Прибыль","Реализация" ,"Списание, конт.","Равномерность продаж" ,"Продажи макс","День продажи макс", "Продажи мин","День продажи мин" ,"Списание макс","День макс списания")
names(table) <- col_headings

# Запись в .csv
write.table(
  table,
  file = '/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица.csv',
  col.names = TRUE,
  row.names = FALSE,
  sep = ';',
  dec = ',',
  fileEncoding = 'UTF-8'
)

# Запись в .xlsx (это чтоб на маке отображалось корректно)
write.xlsx(table,
           file = "/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица.xlsx",
           sheetName = "DATA",
           append = FALSE)