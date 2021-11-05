setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task4')
data <- read.table('./AG.txt', dec=',', header=TRUE)
getwd()
#install.packages('lmtest')
#install.packages("ggiraphExtra")
library(lmtest)
library(ggiraphExtra)

x <- data$x
y <- data$y
x
y



#линейная модель 
m1<-lm(y~x,data=data) 
m1
sm1<-summary(m1) 
sm1
A1 <- (sum(abs(sm1$residuals/y))/length(y))*100

ggPredict(m1, interactive = TRUE)
#данная модель значима
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

#показательная модель
m2<-lm(log10(y)~x,data=data) 
m2 
sm2=summary(m2) 
sm2

A2 <- (sum(abs(sm2$residuals/log10(y)))/length(log10(y)))*100
ggPredict(m2, interactive = TRUE)
#данная модель значима
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

#степенная модель
x1<-log10(x)
y1<-log10(y)
m3<-lm(y1~x1,data=data)
m3
sm3=summary(m3)
sm3

A3 <- (sum(abs(sm3$residuals/y1))/length(y1))*100
ggPredict(m3, interactive = TRUE)
#данная модель значима

#гиперболическая модель
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

x2<-1/x
m4<-lm(y~x2,data=data) 
m4
sm4=summary(m4) 
sm4

A4 <- (sum(abs(sm4$residuals/y))/length(y))*100
ggPredict(m4, interactive = TRUE)

#Линейная
print(sm1$sigma)
print(sm1$r.squared)
print(sm1$fstatistic)
print(A1)


#Показательная
print(sm2$sigma)
print(sm2$r.squared)
print(sm2$fstatistic)
print(A2)

#степенная
print(sm3$sigma)
print(sm3$r.squared)
print(sm3$fstatistic)
print(A3)

#гиперболическая
print(sm4$sigma)
print(sm4$r.squared)
print(sm4$fstatistic)
print(A4)

#данная модель значима
#критерий Стьюдента
#H0 не отвергается, коэффициенты незначимы

#Отчет
#у гиперболической модели самый маленький коэффициент детерминации, а у показательной коэффициент
#R-squared:  0.6878791 (ближе всего к 1), значит,качество данной модели лучшее среди всех остальных