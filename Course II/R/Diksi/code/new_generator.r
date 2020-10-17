
MAX_TRY <- 10000
#Генерация поставок
generate.in <- function(nDays = 7, min = 50, max= 120){
  return(as.integer(runif(n=nDays, min=min,max=max)))
}

#Генерация продаж
generate.out <- function(data.in){
  data.out <- 0
  for(i in 1:length(data.in)){
    data.out[i] <- as.integer(runif(n=1,min=0,max=data.in[i]))
  }
  return(data.out)
}

generate.out2 <- function(data.in, saleLevel = 50){
  
  sum.in <- sum(data.in)
  n <- 0 #счетчик цикла
  repeat{
    n<-n+1
    print(paste("проход №",n))
    
    data.out <- 0
    for(i in 1:length(data.in)){
      data.out[i] <- as.integer(runif(n=1,min=0,max=data.in[i]))
    }
    
    sum.out <- sum(data.out)
    ratio <- round(sum.out /sum.in * 100, 1)
    if (ratio == saleLevel){
      break
    }
  }
  print(paste("Число проходов = ",n))
  return(data.out)
}

generate.out3 <- function(data.in, saleLevel = 50){
  
  sum.in <- sum(data.in)
  n <- 0 #счетчик цикла
  repeat{
    n<-n+1
    print(paste("проход №",n))
    
    data.out <- 0
    for(i in 1:length(data.in)){
      data.out[i] <- as.integer(runif(n=1,min=0,max=data.in[i]))
    }
    
    sum.out <- sum(data.out)
    ratio <- sum.out /sum.in * 100
    
    if ((ratio <= saleLevel * 1.005) && (ratio >= saleLevel * 0.995) || (n == MAX_TRY)){
      break
    }
  }
  print(paste("Число проходов = ",n))
  return(data.out)
}


{
  dataIn <- generate.in(nDays=7,min=40, max=150)
  dataOut <-generate.out3(dataIn,saleLevel = 75)
  print(dataIn)
  print(dataOut)
  
  #считаем процент продаж фактичекий
  saleLevelFact <- round(sum(dataOut)/sum(dataIn) * 100,0.1)
  print(paste0(saleLevelFact,"%"))
}