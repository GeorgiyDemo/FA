setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task4')
data <- read.table('./AG.txt', dec=',', header=TRUE)
getwd()
#install.packages('lmtest')
library(lmtest)

x = data$x
y = data$y
x
y

#линейная модель 
m<-lm(y~x,data=data) 
m 
sm<-summary(m) 
sm 
#данная модель значима
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

#показательная модель
m2<-lm(log10(y)~x,data=data) 
m2 
sm2=summary(m2) 
sm2 
#данная модель значима
#критерий Стьюдента
#H0 отвергается, коэффициенты значимы

#Линейная
print(sm$r.squared)

#Показательная
print(sm2$r.squared)
