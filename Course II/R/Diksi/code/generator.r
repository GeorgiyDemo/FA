#Максимальное число попыток, чтоб сгенерировать данные
MAX_TRY <- 100000
#Уровень продаж в процентах
SALE_LEVELS <-  c(50, 75, 20, 60, 36, 55, 95, 64, 35, 50)
#Позиции товаров
SALE_PRODUCTS <- c("Кофе", "Молоко", "Творог")
#Дни недели
days <-
  c("Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье")

#Генерация поставок для 1 товара
generate.in <- function(nDays = 7,
                        min = 50,
                        max = 120) {
  return(floor((runif(nDays) * ((
    max - min
  ) + 1)) + min))
}

#Генерация продаж
generate.out <- function(data.in, saleLevel = 50) {
  sum.in <- sum(data.in)
  n <- 0 #счетчик цикла
  repeat {
    n <- n + 1
    
    data.out <- 0
    for (i in 1:length(data.in)) {
      data.out[i]  <- floor((runif(1) * ((data.in[i] - 0) + 1)) + 0)
    }
    
    sum.out <- sum(data.out)
    ratio <- sum.out / sum.in * 100
    
    if ((ratio <= saleLevel * 1.005) &&
        (ratio >= saleLevel * 0.995) || (n == MAX_TRY)) {
      break
    }
  }
  
  return(data.out)
}

# Генерация цен товара
generate.price <- function(direction, name.prod) {
  price.tab <-
    #Все заполняем начальными значениями
    data.frame(
      'Продукт' = name.prod,
      'Поставка' = rep(0, length(name.prod)),
      'Продажа' = rep(0, length(name.prod)),
      'Утилизация' = rep(0, length(name.prod))
    )
  
  #Цикл по каждому продукту
  for (prod in (1:length(name.prod))) {
    # Поставка
    price.tab[prod, 2] <- sample(1000:5600, 1)
    # Продажа
    price.tab[prod, 3] <- sample(12500:45000, 1)
    # Утилизация
    price.tab[prod, 4] <- sample(100:300, 1)
  }
  
  #Запись в файл
  write.table(
    price.tab,
    file = direction,
    quote = FALSE,
    row.names = FALSE,
    col.names = TRUE,
    sep = ' ',
    dec = ',',
    fileEncoding = 'UTF-8'
  )
  
}

{
  #Цикл по каждому магазину
  for (i in 1:10) {
    #Закидываем во фрейм поставок
    in.tabl <- data.frame("День недели" = days)
    
    #Закидываем во фрейм продаж
    out.tabl <- data.frame("День недели" = days)
    
    #Цикл по каждому товару
    for (good in SALE_PRODUCTS) {
      #генерируем поставки для конкретного товара
      dataIn <- generate.in(nDays = 7,
                            min = 40,
                            max = 150)
      
      #генерируем продажи для конкретного товара
      dataOut <- generate.out(dataIn, saleLevel = SALE_LEVELS[i])
      
      #Записываем в общий фрейм
      in.tabl <- data.frame(in.tabl, dataIn)
      out.tabl <- data.frame(out.tabl, dataOut)
      
      
      print(paste(
        "Генерация данных по товару",
        good,
        "для магазина",
        i,
        "успешна"
      ))
    }
    
    #Выставляем заголовки
    colnames(in.tabl) <- c("День недели", SALE_PRODUCTS)
    colnames(out.tabl) <- c("День недели", SALE_PRODUCTS)
    
    #Записываем файл поставок
    write.table(
      in.tabl,
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
    
    #Записываем файл продаж
    write.table(
      out.tabl,
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
    
    #Записываем файл цен
    generate.price(
      direction = paste0(
        '/Users/georgiydemo/Projects/FA/Course II/R/Diksi/shop',
        as.character(i),
        '/price.txt'
      ),
      name.prod = SALE_PRODUCTS
    )
    
  }
}
