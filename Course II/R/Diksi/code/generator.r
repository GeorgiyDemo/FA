#Максимальное число попыток, чтоб сгенерировать данные
MAX_TRY <- 10000
#Уровень продаж в процентах
SALE_LEVELS <- c(85,75,20,60,36,55,95,64,35,50)

#Генерация поставок
generate.in <- function(nDays = 7, min = 50, max= 120){
  return(floor((runif(nDays) * ((max - min) + 1)) + min))
}

#Генерация продаж
generate.out <- function(data.in, saleLevel = 50){
  
  sum.in <- sum(data.in)
  n <- 0 #счетчик цикла
  repeat{
    n<-n+1
    
    data.out <- 0
    for(i in 1:length(data.in)){
      data.out[i]  <- floor((runif(1) * ((data.in[i] - 0) + 1)) + 0)
    }
    
    sum.out <- sum(data.out)
    ratio <- sum.out /sum.in * 100
    
    if ((ratio <= saleLevel * 1.005) && (ratio >= saleLevel * 0.995) || (n == MAX_TRY)){
      break
    }
  }
  
  return(data.out)
}

{
  a <- c("Понедельник", "Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
  
  #Цикл по каждому магазину
  for (i in 1:10){
    
    #генерируем поставки
    dataIn <- generate.in(nDays=7,min=40, max=150)
    
    #генерируем продажи
    dataOut <-generate.out(dataIn,saleLevel = SALE_LEVELS[i])
    
    #Закидываем во фрейм поставок
    in.tabl <- data.frame("День недели" = a, "Поставки" = dataIn)
    
    #Закидываем во фрейм продаж
    out.tabl <- data.frame("День недели" = a, "Поставки" = dataOut)
    
    #Записываем файл поставок
    write.table(
      in.tabl,
      file = paste('/Users/georgiydemo/Projects/FA/Course II/R/Diksi/shop',as.character(i),'/in.txt',sep = ''),
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
    
    print(paste("Генерация данных для магазина",i,"успешна"))
  }
}

