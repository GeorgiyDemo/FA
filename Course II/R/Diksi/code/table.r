#install.packages('rJava', type='mac.binary')
#install.packages('xlsx', type='mac.binary')
{
  library("xlsx")
  
  #Устанавливаем директорию
  setwd("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/analytics")
  
  #Цикл по каждому товару. Надеемся на то, что во всех магазах одинаковые товары
  goods.table <- read.table(file = 'store1_price.txt', head = TRUE)
  goods <- goods.table[, 1]
  
  ############ Работаем только с таблицей .csv и .xlsx #########################
  
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
  
  ######################## Формируем графики ###################################
  
  #TODO Вектор всех возможных цветов для построения товаров
  plot_colors <- c("red3","forestgreen", "steelblue", "darkgreen","darkolivegreen3", "darkorange1","firebrick1","gold1", "lightcoral","mediumvioletred","navyblue", "tan1","turquoise1","chocolate1","blue","black","brown", "darkseagreen" )
  #TODO Вектор всех возможных значков для товаров
  plot_pchs <- rev(seq(1:25))
  
  #Общая выручка со всех магазинов и со всех продуктов
  super_summ_shoprevenue  <- rep(0,7)
  #Общая прибыль со всех магазинов и со всех продуктов
  super_summ_shopprofits <- rep(0,7)
  #Общее списание со всех магазинов и со всех продуктов
  super_summ_writeoffs <- rep(0,7)
  
  #Датафрейм с прибылью
  super_df_shopprofits <- data.frame(buf=rep(0,7))
  #Датафрейм с рентабельностью
  super_df_profitability <- data.frame(buf=rep(0,7))
  
  
  #Цикл по каждому магазу
  for (i in 1:10) {
    in1 <- read.table(file = paste0('store',as.character(i),'_in.txt'), head = TRUE)
    out1 <- read.table(file = paste0('store',as.character(i),'_out.txt'), head = TRUE)
    price1 <- read.table(file = paste0('store',as.character(i),'_price.txt'), head = TRUE)
    
    #Общая выручка со всех продуктов
    summ_shopprofits <- rep(0,7)
    summ_shoprevenue <- rep(0,7)
    summ_writeoffs <- rep(0,7)
    
    
    #Датафреймы по каждому продукту для вывода единых графиков с несколькими продуктами
    #объем продаж
    df_salesvolume <- data.frame(buf=rep(0,7))
    #выручка
    df_shoprevenue <- data.frame(buf=rep(0,7))
    #прибыль
    df_shopprofits <- data.frame(buf=rep(0,7))
    #Списание
    df_writeoffs <- data.frame(buf=rep(0,7))
    #Рентабельность
    df_profitability <- data.frame(buf=rep(0,7))
    
    #Цикл по каждому продукту в каждом магазине
    for (prod in goods){
    
      element_index <- which(goods.table == prod)
      #Цена продажи
      product_price <- goods.table[element_index, 3]
      #Цена поставки
      supply_price <- goods.table[element_index, 2]
      #Цена утилизации
      util_price <- goods.table[element_index, 4]
      
      # Выручка
      buf_shoprevenue <- product_price * out1[, prod]
      png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Выручка магазин ",as.character(i)," (",prod,").png"),width=600, height=450)
      plot(buf_shoprevenue, main=paste0('Выручка по дням в магазине ',as.character(i),' (',prod,')'), xlab='День', ylab=paste0("Выручка по товару '",prod,"', руб."),type='o')
      dev.off()
      
      # Списание
      buf_writeoff <- in1[, prod] - out1[, prod]
      xrange <- range(seq(1,7))
      yrange <- range(buf_writeoff)
      png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Списание магазин ",as.character(i)," (",prod,").png"),width=600, height=450)
      plot(xrange,
           yrange,
           main=paste0('Списание ',prod,' в ',as.character(i),' магазине'), 
           xlab="День", 
           ylab="Списание, шт.",
           type = "n"
           )
      points(seq(1,7), buf_writeoff, pch=19, col="red")
      lines(seq(1,7), buf_writeoff, pch=19, col="black")
      dev.off()
      
      # Затраты
      buf_cost <- (in1[, prod] * supply_price) + (buf_writeoff * util_price)
      # Прибыль
      shop_profits <- buf_shoprevenue - buf_cost
      
      png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Прибыль магазин ",as.character(i)," (",prod,").png"),width=600, height=450)
      plot(shop_profits, main=paste0('Прибыль по дням в ',as.character(i),' магазине (',prod,')'), xlab='День', ylab='Прибыль, .руб.',type='S')
      dev.off()
      
      #Добавляем данные во фреймы для построения графиков ниже
      #Объём продаж
      df_salesvolume <- data.frame(df_salesvolume, out1[, prod])
      #выручка
      df_shoprevenue <- data.frame(df_shoprevenue, buf_shoprevenue)
      #прибыль
      df_shopprofits <- data.frame(df_shopprofits, shop_profits)
      #Списание
      df_writeoffs <- data.frame(df_writeoffs, buf_writeoff)
      #Рентабельность
      df_profitability <- data.frame(df_profitability, floor((shop_profits/buf_shoprevenue) * 100))
      
      
      #Прибавляем к сумме выручки
      summ_shoprevenue <- summ_shoprevenue + buf_shoprevenue
      #Прибавляем к сумме прибыли
      summ_shopprofits <- summ_shopprofits + shop_profits
      #Прибавляем к сумме списаний
      summ_writeoffs <- summ_writeoffs + buf_writeoff
      
    }
    
    ############################################Графики с несколькими товарами на одном графике##########################
    
    #График объёма продаж товарав в первом магазине по дням
    df_salesvolume <- subset(df_salesvolume, select = -c(buf))
    names(df_salesvolume) <- goods
    xrange <- range(seq(1,7))
    yrange <- range(df_salesvolume)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Объём продаж магазин ",as.character(i),".png"),width=600, height=450)
    graph <- plot(xrange,
                  yrange,
                  main=paste0('Объём продаж в магазине ',as.character(i)," по товарам"), 
                  xlab="День недели", 
                  ylab="Количество проданного товара, шт",
                  type = "n",
    )
    for (j in 1:length(goods)){
      points(seq(1,7),df_salesvolume[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
      lines(seq(1,7), df_salesvolume[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
    }
    legend("topright", legend=goods,col=plot_colors, pch=plot_pchs)
    dev.off()
    
    #График выручки от товарав по дням
    df_shoprevenue <- subset(df_shoprevenue, select = -c(buf))
    names(df_shoprevenue) <- goods
    xrange <- range(seq(1,7))
    yrange <- range(df_shoprevenue)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Выручка магазин ",as.character(i),".png"),width=600, height=450)
    graph <- plot(xrange,
                  yrange,
                  main=paste0('Выручка в магазине ',as.character(i)," по товарам"), 
                  xlab="День недели", 
                  ylab="Выручка, руб",
                  type = "n",
    )
    for (j in 1:length(goods)){
      points(seq(1,7),df_shoprevenue[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
      lines(seq(1,7), df_shoprevenue[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
    }
    legend("topright", legend=goods,col=plot_colors, pch=plot_pchs)
    dev.off()

    # График прибыли от товарав по дням
    df_shopprofits <- subset(df_shopprofits, select = -c(buf))
    names(df_shopprofits) <- goods
    xrange <- range(seq(1,7))
    yrange <- range(df_shopprofits)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Прибыль магазин ",as.character(i),".png"),width=600, height=450)
    graph <- plot(xrange,
                  yrange,
                  main=paste0('Прибыль в магазине ',as.character(i)," по товарам"), 
                  xlab="День недели", 
                  ylab="Прибыль, руб",
                  type = "n",
    )
    for (j in 1:length(goods)){
      points(seq(1,7),df_shopprofits[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
      lines(seq(1,7), df_shopprofits[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
    }
    legend("topright", legend=goods,col=plot_colors, pch=plot_pchs)
    dev.off()

    # График списания товарав по дням
    df_writeoffs <- subset(df_writeoffs, select = -c(buf))
    names(df_writeoffs) <- goods
    xrange <- range(seq(1,7))
    yrange <- range(df_writeoffs)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Списания магазин ",as.character(i),".png"),width=600, height=450)
    graph <- plot(xrange,
                  yrange,
                  main=paste0('Списания в магазине ',as.character(i)," по товарам"), 
                  xlab="День недели", 
                  ylab="Количество списанного товара, шт",
                  type = "n",
    )
    for (j in 1:length(goods)){
      points(seq(1,7),df_writeoffs[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
      lines(seq(1,7), df_writeoffs[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
    }
    legend("topright", legend=goods,col=plot_colors, pch=plot_pchs)
    dev.off()

    # График рентабельности товарав по дням
    df_profitability <- subset(df_profitability, select = -c(buf))
    names(df_profitability) <- goods
    xrange <- range(seq(1,7))
    yrange <- range(df_profitability)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Рентабельность магазин ",as.character(i),".png"),width=600, height=450)
    graph <- plot(xrange,
                  yrange,
                  main=paste0('Рентабельность в магазине ',as.character(i)," по товарам"), 
                  xlab="День", 
                  ylab="Рентабельность, %",
                  type = "n"
    )
    for (j in 1:length(goods)){
      points(seq(1,7),df_profitability[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
      lines(seq(1,7), df_profitability[, goods[j]], pch=plot_pchs[j], col=plot_colors[j])
    }
    legend("topright", legend=goods,col=plot_colors, pch=plot_pchs)
    dev.off()
    
    #Строим общий график выручки по дням
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Общая выручка магазин ",as.character(i),".png"),width=600, height=450)
    plot(summ_shoprevenue, main=paste0('Выручка по дням в магазине ',as.character(i)), xlab='День', ylab=paste0("Общая выручка, руб."),type='o')
    dev.off()
    
    #Строим общий график прибыли по дням
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Общая прибыль магазин ",as.character(i),".png"),width=600, height=450)
    plot(summ_shopprofits, main=paste0('Прибыль по дням в магазине ',as.character(i)), xlab='День', ylab='Общая прибыль, руб.',type='S')
    dev.off()
    
    #Строим общий график списаний по дням
    xrange <- range(seq(1,7))
    yrange <- range(summ_writeoffs)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Общее списание магазин ",as.character(i),".png"),width=600, height=450)
    plot(xrange,yrange,main=paste0('Списания по дням в ',as.character(i),' магазине'), xlab="День", ylab="Списание, шт.", type = "n")
    points(seq(1,7), summ_writeoffs, pch=19, col="red")
    lines(seq(1,7), summ_writeoffs, pch=19, col="black")
    dev.off()
    
    #Строим график рентабельности для магазина
    summ_profitability <- floor((summ_shopprofits/summ_shoprevenue) * 100)
    xrange <- range(seq(1,7))
    yrange <- range(summ_profitability)
    png(file=paste0("/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/shop",as.character(i),"/Общая рентабельность магазин ",as.character(i),".png"),width=600, height=450)
    plot(xrange,
         yrange,
         main=paste("Рентабельность по дням в",as.character(i),"магазине"), 
         xlab="День", 
         ylab="Рентабельность, %",
         type = "n"
    )
    lines(seq(1,7), summ_profitability, pch=20, col="red3",lwd = 3, lty = 2)
    dev.off()
    
    
    #Прибавляем выручку к общей выручке
    super_summ_shoprevenue <- super_summ_shoprevenue + summ_shoprevenue
    #Прибавляем прибыль к общей прибыли
    super_summ_shopprofits <- super_summ_shopprofits + summ_shopprofits
    #Прибавляем списания к общим списаниям
    super_summ_writeoffs <- super_summ_writeoffs + summ_writeoffs
    
    #Прибавляем к датафрейму рентабельности
    super_df_profitability <- data.frame(super_df_profitability, summ_profitability)
    #Прибавляем к датафрейму прибыли
    super_df_shopprofits <- data.frame(super_df_shopprofits, summ_shopprofits)
  
  }
  
  #Строим график общей выручки
  super_summ_shoprevenue1 <- super_summ_shoprevenue / 1000
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общая выручка.png", width=600, height=450)
  plot(super_summ_shoprevenue1, main='Выручка во всех магазинах по дням', xlab='День', ylab="Общая выручка, тыс руб.",type='o')
  dev.off()
  
  #Строим график общей прибыли
  super_summ_shopprofits1 <- super_summ_shopprofits / 1000
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общая прибыль.png", width=600, height=450)
  plot(super_summ_shopprofits1, main='Прибыль во всех магазинах по дням', xlab='День', ylab='Общая прибыль, тыс руб.',type='S')
  dev.off()
  
  #Строим график общих списаний
  xrange <- range(seq(1,7))
  yrange <- range(super_summ_writeoffs)
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общее списание.png",width=600, height=450)
  plot(xrange,yrange,main='Списание во всех магазинах по дням', xlab="День", ylab="Списание, шт.", type = "n")
  points(seq(1,7), super_summ_writeoffs, pch=19, col="red")
  lines(seq(1,7), super_summ_writeoffs, pch=19, col="black")
  dev.off()
  
  #Строим график рентабельности
  super_summ_profitability <- floor((super_summ_shopprofits/super_summ_shoprevenue) * 100)
  xrange <- range(seq(1,7))
  yrange <- range(super_summ_profitability)
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общая рентабельность.png",width=600, height=450)
  plot(xrange,
       yrange,
       main="Рентабельность по дням общая", 
       xlab="День", 
       ylab="Рентабельность, %",
       type = "n"
  )
  lines(seq(1,7), super_summ_profitability, pch=20, col="red3",lwd = 3, lty = 2)
  dev.off()
  
  ########################Строим сложный график рентабельности##########################
  #Выкидываем нулевой столбец
  super_df_profitability <- subset(super_df_profitability, select = -c(buf))
  #Присваиваем имена столбцам для обращения по ним
  names(super_df_profitability) <- paste0("shop",as.character(seq(1:10)))
  xrange <- range(seq(1,7))
  yrange <- range(super_df_profitability)
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общая рентабельность подробно.png",width=716, height=630)
  plot(xrange,
       yrange,
       main='Рентабельность по дням в магазинах', 
       xlab="День", 
       ylab="Рентабельность, %",
       type = "n"
    )
  for (i in 1:length(super_df_profitability)){
    points(seq(1,7), super_df_profitability[,paste0("shop",as.character(i))], pch=19, col=plot_colors[i])
  }
  legend("bottomleft", legend=paste("Магазин", seq(1:10)),col=plot_colors,pch=c(19))
  dev.off()
  
  ########################Строим сложный график прибыли##########################
  #Выкидываем нулевой столбец
  super_df_shopprofits <- subset(super_df_shopprofits, select = -c(buf))
  #Присваиваем имена столбцам для обращения по ним
  names(super_df_shopprofits) <- paste0("shop",as.character(seq(1:10)))
  super_df_shopprofits <- super_df_shopprofits / 1000
  xrange <- range(seq(1,7))
  yrange <- range(super_df_shopprofits)
  png(file="/Users/georgiydemo/Projects/FA/Course II/R/Diksi/result/graph/Общая прибыль подробно.png",width=716, height=630)
  plot(xrange,
       yrange,
       main='Прибыль по дням в магазинах', 
       xlab="День", 
       ylab="Прибыль, тыс руб",
       type = "n"
  )
  for (i in 1:length(super_df_shopprofits)){
    points(seq(1,7), super_df_shopprofits[,paste0("shop",as.character(i))], pch=18, col=plot_colors[i], cex=2.0)
  }
  legend("bottomleft", legend=paste("Магазин", seq(1:10)),col=plot_colors,pch=c(18))
  dev.off()

  print("Завершение работы скрипта")
  
}