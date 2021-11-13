#Оценить коэффициенты регрессии с помощью процедуры Кохрейна – Оркатта на примере данных о
#динамике золотовалютных резервов РФ за период с 26.12.03 по 07.01.05 (task1.txt).
#X –  время, отсчитываемое в днях от начального момента времени 26.12.03,
#а столбец Y – золотовалютные резервы (в млрд долл.).

#install.packages("lmtest")
#install.packages("forecast")
#install.packages("tseries")
#install.packages("orcutt")
#install.packages("orcutt")
library(orcutt)
library(lmtest)
library(forecast)
library(tseries)
library(orcutt)
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract11")


data <- read.table('task1.txt',  header=TRUE)
x <- data$X; x
y <- data$Y; y

# Множественная модель
p_many <- lm(y~x)
s_many <- summary(p_many)
s_many


dw <- dwtest(p_many) # Тест Дарбина-Ватсона
#DW стремится к 0
#p-value < 2.2e-16 меньше всех уровней значимостей
#H0 отвергается

bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0 отвергаем, автокорреляция присутствует
bgtest(p_many, order = 2, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0 отвергаем, автокорреляция присутствует

gqtest(p_many, order.by = x1, fraction = 0.25) # Тест Голдфельда-Квандта для x1
#H0 принимается
bptest(p_many, studentize = TRUE) # Тест Бреуша-Пагана
#H0 отвергается


y3<-y/predict(p_many)
x3<-x/predict(p_many)
m3<-lm(y3~x3)
s3<-summary(m3)
s3


cochrane.orcutt(p_many)


DW<-dw$statistic
DW
p<-1-DW/2;p

y

y4<-y[2:55]-p*y[1:54]
y4
x4<-x[2:55]-p*x[1:54]
x4

m4<-lm(y4~x4);m4
s4<-summary(m4);s4

a <- s4$coefficients[1]/(1-p);a
b <- s4$coefficients[2]; b

dwtest(m4) # Тест Дарбина-Ватсона

bgtest(m4, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0 принимается, автокорреляция первого порядка отсутствует
bgtest(m4, order = 2, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0 принимается, автокорреляция первого порядка отсутствует

gqtest(m4, order.by = x4, fraction = 0.25) # Тест Голдфельда-Квандта для x1
#отсутствует проблема гетероскедастичности а уровне 0.01

bptest(m4, studentize = TRUE) # Тест Бреуша-Пагана
#отсутствует проблема гетероскедастичности на всех уровнях
