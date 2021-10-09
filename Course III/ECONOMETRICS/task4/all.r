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

ggPredict(m1, interactive = TRUE)
#данная модель значима
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

#показательная модель
m2<-lm(log10(y)~x,data=data) 
m2 
sm2=summary(m2) 
sm2 

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
ggPredict(m4, interactive = TRUE)

#Линейная
print(sm1$r.squared)

#Показательная
print(sm2$r.squared)

#степенная
print(sm3$r.squared)

#гиперболическая
print(sm4$r.squared)

#данная модель значима
#критерий Стьюдента
#H0 не отвергается, коэффициенты незначимы

#Отчет
#у гиперболической модели самый маленький коэффициент детерминации, а у показательной коэффициент
#R-squared:  0.6878791 (ближе всего к 1), значит,качество данной модели лучшее среди всех остальных