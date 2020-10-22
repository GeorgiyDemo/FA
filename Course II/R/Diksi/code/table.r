#install.packages('rJava', type='mac.binary')
#install.packages('xlsx', type='mac.binary')
{
  library("xlsx")
  
  #Устанавливаем директорию
  setwd("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/analytics")
  
  #Цикл по каждому товару. Надеемся на то, что во всех магазах одинаковые товары
  goods.table <- read.table(file = 'store1_price.txt', head = TRUE)
  goods <- goods.table[, 1]
  
  for (prod in goods) {
    #Индекс продукта
    element_index <- which(goods.table == prod)
    #Цена продажи
    product_price <- goods.table[element_index, 3]
    #Цена поставки
    supply_price <- goods.table[element_index, 2]
    #Цена утилизации
    util_price <- goods.table[element_index, 4]
    
    #Названия магазинов
    shop_names <- c()
    #Выручка
    shop_revenues <- c()
    #Прибыль
    shop_profits <- c()
    #Реализация
    shop_sales <- c()
    #Списание
    shop_writeoffs <- c()
    #Равномерность продаж
    shop_sr <- c()
    #Продажи макс
    shop_sales_max <- c()
    #День продажи макс
    shop_sales_maxdays <- c()
    #Продажи мин
    shop_sales_min <- c()
    #День продажи мин
    shop_sales_mindays <- c()
    #Списание макс
    shop_writeoff_max <- c()
    #День списания макс
    shop_writeoff_maxdays <- c()
    
    
    #Цикл по каждому магазину
    for (i in 1:10) {
      in1 <-
        read.table(file = paste0('store', as.character(i), '_in.txt'),
                   head = TRUE)
      
      print(in1)
      out1 <-
        read.table(file = paste0('store', as.character(i), '_out.txt'),
                   head = TRUE)
      
      
      # Название магазина
      shop_names <-
        append(shop_names, paste0('shop', as.character(i)))
      
      # Списание
      buf_writeoff <- sum(in1[, prod]) - sum(out1[, prod])
      shop_writeoffs <- append(shop_writeoffs, buf_writeoff)
      
      # Выручка
      buf_shoprevenue <- product_price * sum(out1[, prod])
      shop_revenues <- append(shop_revenues, buf_shoprevenue)
      
      # Затраты
      buf_cost <-
        (sum(in1[, prod]) * supply_price) + (buf_writeoff * util_price)
      
      # Прибыль
      shop_profits <-
        append(shop_profits, buf_shoprevenue - buf_cost)
      
      # Реализация
      shop_sales <- append(shop_sales, sum(out1[, prod]))
      
      # Равномерность продаж
      shop_sr <- append(shop_sr, sd(out1[, prod]))
      
      # Продажи макс
      shop_sales_max <- append(shop_sales_max, max(out1[, prod]))
      
      # День продажи макс
      shop_sales_maxdays <-
        append(shop_sales_maxdays, out1[which.max(out1[, prod]), 1])
      
      # Продажи мин
      shop_sales_min <- append(shop_sales_min, min(out1[, prod]))
      
      # День продажи мин
      shop_sales_mindays <-
        append(shop_sales_mindays, out1[which.min(out1[, prod]), 1])
      
      # Списание макс
      shop_writeoff_max <-
        append(shop_writeoff_max, max(c(in1[, prod] - out1[, prod])))
      
      # День списания макс
      shop_writeoff_maxdays <-
        append(shop_writeoff_maxdays, in1[which.max(c(in1[, prod] - out1[, prod])), 1])
    }
    
    
    #График по прибыли магазинов в зависимости от дня недели
    barplot(shop_sales_min, horiz=TRUE)
    
    

    
    #Высчитываем итог и среднее для выручки, прибыли, реализации, списании, равномерности
    shop_names <- c(shop_names, c("Итог", "Среднее"))
    shop_revenues <-
      c(shop_revenues, c(sum(shop_revenues), mean(shop_revenues)))
    shop_profits <-
      c(shop_profits, c(sum(shop_profits), mean(shop_profits)))
    shop_sales <-
      c(shop_sales, c(sum(shop_sales), mean(shop_sales)))
    shop_writeoffs <-
      c(shop_writeoffs, c(sum(shop_writeoffs), mean(shop_writeoffs)))
    shop_sr <- c(shop_sr, c(sum(shop_sr), mean(shop_sr)))
    shop_sales_max <- c(shop_sales_max, c("", ""))
    shop_sales_maxdays <- c(shop_sales_maxdays, c("", ""))
    shop_sales_min <- c(shop_sales_min, c("", ""))
    shop_sales_mindays <- c(shop_sales_mindays, c("", ""))
    shop_writeoff_max <- c(shop_writeoff_max, c("", ""))
    shop_writeoff_maxdays <- c(shop_writeoff_maxdays, c("", ""))
    
    #Формируем датафрейм
    table <-
      data.frame(
        shop_names,
        shop_revenues,
        shop_profits,
        shop_sales ,
        shop_writeoffs,
        shop_sr,
        shop_sales_max,
        shop_sales_maxdays,
        shop_sales_min,
        shop_sales_mindays,
        shop_writeoff_max,
        shop_writeoff_maxdays
      )
    
    #Проставляем заголовки
    col_headings <-
      c(
        "Магазин" ,
        "Выручка, руб" ,
        "Прибыль",
        "Реализация" ,
        "Списание, конт.",
        "Равномерность продаж" ,
        "Продажи макс",
        "День продажи макс",
        "Продажи мин",
        "День продажи мин" ,
        "Списание макс",
        "День макс списания"
      )
    names(table) <- col_headings
    
    # Запись в .csv
    write.table(
      table,
      file = paste0(
        "/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица_",
        prod,
        ".csv"
      ),
      col.names = TRUE,
      row.names = FALSE,
      sep = ';',
      dec = ',',
      fileEncoding = 'UTF-8'
    )
    
    # Запись в .xlsx (это чтоб на маке отображалось корректно)
    write.xlsx(
      table,
      file = paste0(
        "/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/таблица_",
        prod,
        ".xlsx"
      ),
      sheetName = "DATA",
      col.names = TRUE,
      row.names = FALSE,
      append = FALSE
    )
  }
}
