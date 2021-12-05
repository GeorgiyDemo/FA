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
#yреал_30=201.65; yреал_30∈(200.6833;202.6823) - предиктивный
#yреал_30=201.65; yреал_30∈(201.3126;202.0529) - доверительный
#Модель адекватна по обоим интервалам

elm1 = coef(m)[2]*(mean(data$))