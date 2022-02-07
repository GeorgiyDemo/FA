library(forecast)
library(tseries)
library(lmtest)
library(car)

setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/pract9/task2/Сезонные составляющие')
data <- read.csv('./data_fict.csv', sep = ";")
data2 <- read.csv('./data_fict.csv', sep = ";")
data3 <- read.csv('./data_season.csv', sep = ";")
data

y <- data$IP
x <- data$t
cor(data)

p_many <- lm(y~x)
s_many <- summary(p_many)
e <- s_many$residuals
e
s_many

A_many <- sum(abs(s_many$residuals/y)) / length(y) * 100 # Апроксимация
A_many
error_many <- sqrt(deviance(p_many)/df.residual(p_many))

determ <- s_many$r.squared
adjust_determ <- s_many$adj.r.squared
st_error <- error_many
approx <- A_many
f_test <- s_many$fstatistic[1]

data['e'] = data.frame(e)
data['Остаток'] = 0

#Работа с устреденеием остатков
ost1 = sum(data[data$Квартал == 1,]$e)/10
ost1

ost2 = sum(data[data$Квартал == 2,]$e)/10
ost2

ost3 = sum(data[data$Квартал == 3,]$e)/10
ost3

ost4 = sum(data[data$Квартал == 4,]$e)/10
ost4

# Добавление столбца с сезонными составляющими-остатками
data[data$Квартал == 1,]$Остаток = ost1
data[data$Квартал == 2,]$Остаток = ost2
data[data$Квартал == 3,]$Остаток = ost3
data[data$Квартал == 4,]$Остаток = ost4

data$IP <- (data$IP - data$Остаток)
m2 = lm(IP~t, data=data2)

plot(data$IP) #график

#прогнозирование по модели 
predictIP = predict(m2, newdata = data3)
predictIP

data3['Прогнозирование'] = data.frame(predictIP)
data3

write.csv(data3,"./data_season_results.csv", row.names = TRUE)

