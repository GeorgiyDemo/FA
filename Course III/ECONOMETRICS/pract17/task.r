#install.packages("lmtest")
#install.packages("forecast")
#install.packages("tseries")
#install.packages("orcutt")
#install.packages("psych")
library(orcutt)
library(lmtest)
library(forecast)
library(tseries)
library(orcutt)
library(psych)
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract17")

data <- read.csv('./data.csv', sep = ";"); data
train <- data[1:29,]; train
test <- data[30:30,]; test

Q <- train$Q; Q
I <- train$I; I
M <- train$M; M
P <- train$P; P


p_many <- lm(Q~I+M+P)
s_many <- summary(p_many)
s_many

cor(train)

#######В) Проверьте значимость модели регрессии в целом и каждого коэффициента модели по отдельности.######
determ <- s_many$r.squared
adjust_determ <- s_many$adj.r.squared
st_error <- sqrt(deviance(p_many)/df.residual(p_many))
approx <- sum(abs(s_many$residuals/Q)) / length(Q) * 100
f_test <- s_many$fstatistic[1]

compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)
print(compare)
#R^2 = 0.8234058 - качество отличное
# Se = 0.450804 - качество хорошее
# Ош аппроксимации = 0.1630103 -  качество отличное
#Вывод: модель хороша 

test
predict(p_many, newdata = test, interval = "confidence", level = 0.95);
predict(p_many, newdata = test, interval = "prediction", level = 0.95);
#201.65 -> 201.3126 202.0529

#yреал_30=201.65; yреал_30 принадлежит (200.6833;202.6823) - предиктивный
#yреал_30=201.65; yреал_30 не принадлежит (201.3126;202.0529) - доверительный
#Модель адекватна по одному из параметров интервалам

#С ростом дохода на 1000 объем увеличится,
#вне зависимости ни от чего объем продаж (объем потребления) 166,6 млн

el1 <- s_many$coefficients[2] * mean(I) / mean(Q); el1
#0.1904783 -> не эластично
el2 <- s_many$coefficients[3] * mean(M) / mean(Q); el2
#0.01558067 -> не эластично
el3 <- s_many$coefficients[4] * mean(P) / mean(Q); el3
#-0.03635037 -> не эластично
# Все не эластично!!!

#Анализ матриц парных корреляций;
cor(train)
corr.test(train, alpha=0.05)

m_i = lm(I ~ M+P, data = train) 
m_m = lm(M ~ I+P, data = train) 
m_p = lm(P ~ M+I, data = train)