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
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract13")

data <- read.csv('./tema7.csv', sep = ";", dec=",")
train <- data[1:20,]; train
test <- data[21:22,]; test

x1 <- train$x1; x1
x2 <- train$x2; x2
x3 <- train$x3; x3
x4 <- train$x4; x4
y <- train$y; y

p_many <- lm(y~x1+x2+x3+x4)
s_many <- summary(p_many)
s_many

cor(train)

#######В) Проверьте значимость модели регрессии в целом и каждого коэффициента модели по отдельности.######
determ <- s_many$r.squared
adjust_determ <- s_many$adj.r.squared
st_error <- sqrt(deviance(p_many)/df.residual(p_many))
approx <- sum(abs(s_many$residuals/y)) / length(y) * 100
f_test <- s_many$fstatistic[1]

compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)
print(compare)
#Вывод о качестве: модель качественная, R^2 приближен к 1

test
predict(p_many, newdata = test, interval = "confidence", level = 0.95);
predict(p_many, newdata = test, interval = "prediction", level = 0.95);
#Модель неадекватна по обоим интервалам


p_many2 <- lm(y~x1+x2+x4)
s_many2 <- summary(p_many2)
s_many2

test
predict(p_many2, newdata = test, interval = "confidence", level = 0.95);
predict(p_many2, newdata = test, interval = "prediction", level = 0.95);

p_many3 <- lm(y~x1+x4)
s_many3 <- summary(p_many3)
s_many3

test
predict(p_many3, newdata = test, interval = "confidence");
predict(p_many3, newdata = test, interval = "prediction");


o1=train[1:10,];o1

x1 <- n1$x1; x1
x2 <- n1$x2; x2
x3 <- n1$x3; x3
x4 <- n1$x4; x4
y <- n1$y; y

p1 <- lm(y~x1+x2+x3+x4, data=o1)
s1 <- summary(p_many)
s1

o2=train[11:20,];o2

x1 <- n2$x1; x1
x2 <- n2$x2; x2
x3 <- n2$x3; x3
x4 <- n2$x4; x4
y <- n2$y; y

p2 <- lm(y~x1+x2+x3+x4, data=o2)
s2 <- summary(p_many)
s2

RSS <- sum(p_many$residuals^2); RSS
RSS1 <- sum(p1$residuals^2); RSS1
RSS2 <- sum(p2$residuals^2); RSS2


n1=length(o1$x1);n1
n2=length(o2$x1);n2
x=train[,-5]
k=length(x);k
Chow=(RSS-RSS1-RSS2)*(n1+n2-2*(k+1))/(k+1)/(RSS1+RSS2);Chow
#Fstat
qf(0.95,k+1,n1+n2-2*(k+1))
#выборки однородны

cor(train) #x4 с y имеют самую тесную взаимосвязь

#проверяем остатки на нормальность
ost = s_many$residuals
ost


jarque.bera.test(ost)
#h0- остатки нормально распределены
#h1-остатки ненормально распределены

#P-val > alpha; h0 принимаем, остатки норм распределены

cor(data)

#строим парную модель по y и x4
p4 = lm(y~x4); p4
s4 <- summary(p4); s4


#Проводим тест вальда
waldtest(p_many, p4)
#H0: короткая модель
#Н1: длинная модель
qf(0.95,3,20-5)
#Fнабл > Fкр -> h1, длинная модель

#Тест Рамсея для полной модели (т.к. модель длинная)
resettest(p_many)
#принимаем H0, так как pvalue=0.3814 => нет пропущенных переменных



#####################################################


#Тест РАМСЕЯ
y_m = predict(p_many)
y_m

y_m2 = y_m^2
y_m2

y_m3 = y_m^3
y_m3

p_new_ramsey = lm(y~x1+x2+x3+x4+y_m2+y_m3)
p_new_ramsey

sm_ramsey = summary(p_new_ramsey)
sm_ramsey

#Проводим тест вальда для Новой модели с 6 факторами и старой модели с 4 факторами
waldtest(p_new_ramsey, p_many)

resettest(p_new_ramsey)

resettest(p_many)