# install.packages('lmtest')
# install.packages('car')
#install.packages("tseries")
#install.packages("forecast")
library(forecast)
library(tseries)
library(lmtest)
library(car)

setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task8')
data <- read.csv('./check.csv', sep = ";")

y <- data$GDP
x1 <- data$t
x2 <- data$d1
x3 <- data$d2
x4 <- data$d3

# Корреляционная матрица
cor(data) 

# Диаграммы рассеяния
plot(y, x1, col = 'red')
plot(y, x2, col= 'blue')
plot(y, x3, col = 'green')
plot(y, x4, col = 'yellow')

########################################################################################
# Множественная модель
p_many <- lm(y~x1+x2+x3+x4)
s_many <- summary(p_many)
s_many

A_many <- sum(abs(s_many$residuals/y)) / length(y) * 100 # Апроксимация
A_many

confint(p_many, level = 0.95) # Доверительные интервалы

# Сравнение моделей
determ <- s_many$r.squared
adjust_determ <- s_many$adj.r.squared
st_error <- error_many
approx <- A_many
f_test <- s_many$fstatistic[1]

#######В) Проверьте значимость модели регрессии в целом и каждого коэффициента модели по отдельности.######
compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)
print(compare)

"
Качество модели хорошее:
Модель очень качественная R^2 = 0.9628084
R^2 = 0.9628 (приближено к 1)
Se = 1051 (относительно у не очень много — качество нормальное (умеренное отношение))
F = 226.5
p-value = < 2.2e-16
Ошибка_аппроксимации < 7 - модель хорошая (5.371801)
"


#прогнозирование по модели с фиктивными переменными
pred=data.frame(c(41,42,43),c(1,0,0),c(0,1,0),c(0,0,1))
colnames(pred)=c("x1","x2","x3","x4")
predictGDP=predict(p_many, newdata = pred)
predictGDP
pred


dwtest(p_many) # Тест Дарбина-Ватсона
#  2.676e-08
bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#pv 4.028e-06 > 0.1,0.05, 0.01 =>H0 принимается, автокорреляция первого порядка отсутствует

gqtest(p_many, order.by = x1, fraction = 0) # Тест Голдфельда-Квандта для x1
#p-value = 0.1982 - больше 0.1 0.05 0.01, отсутствует проблема гетероскедастичности

bptest(p_many, studentize = TRUE) # Тест Бреуша-Пагана
#p-value = 0.546, - больше 0.1 0.05 0.01, отсутствует проблема гетероскедастичности

error_many <- sqrt(deviance(p_many)/df.residual(p_many))

#работа с временным рядом GDP 
GDP <- c(data$GDP)
GDP1 <- ts(data=GDP,start=c(2009), name="GDP", frequency = 4)
GDP1
ACF <- Acf(GDP1) # выборочная автокорреляция
ACF
PACF <- Pacf(GDP1) # частная автокорреляиця 
PACF
tsdisplay(GDP1)
#вывод: ряд нестационарный