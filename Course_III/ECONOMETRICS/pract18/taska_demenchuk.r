#install.packages("forecast")
#install.packages("lmtest")
#install.packages("tseries")
#install.packages("urca")
library(urca)
library(lmtest)
library(tseries)
library(forecast)

# Получение данных
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract18")
data <- read.csv('./data.csv', sep = ";"); data

#Построение лага
lag <- data.frame(
  y = data$y[3:length(data$y)],
  x0 = data$x[3:length(data$y)],
  x1 = data$x[2:(length(data$y) - 1)],
  x2 = data$x[1:(length(data$y) - 2)]
)
lag

#Разадление выборки на тренировочную и проверочную
train <- lag[1:(length(lag$y) - 1),]
test <- lag[(length(lag$y)):length(lag$y),]

#Формируем модель
p_many <- lm(y ~ x0 + x1 + x2, data = train)
s_many <- summary(p_many)
s_many

determ <- round(s_many$r.squared, 3)
adjust_determ <- round(s_many$adj.r.squared, 3)
st_error <- round(sqrt(deviance(p_many)/df.residual(p_many)), 3)
approx <- round(sum(abs(s_many$residuals/data$y)) / length(data$y) * 100, 3)
f_test <- round(s_many$fstatistic[1], 3)

compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)
print(compare)

#Тесты
#Проверка на проблему гетероскедастичности
gqtest(p_many, fraction = 0.3)
#GQ = NaN, df1 = 1, df2 = 0, p-value = NA
#p-value = NA ??????? (0.1; 0.05; 0.01), надо другой fracetion выставлять

bptest(p_many)
#Гомоскедастичность – H0
#Гетероскедастичность - Hа
#BP = 4.6214, df = 3, p-value = 0.2017
#p-value = 0.2017 > (0.1; 0.05; 0.01), отсутствует проблема гетероскедастичности
#ВЫВОД: Нет проблем гетероскедастичности, ряд гомоскедастичен


#Проверка на авторкорреляцию
dwtest(p_many) # Тест Дарбина-Ватсона
#H0: нет автокорреляции
#Ha: есть автокорреляция 1-го порядка
#DW = 0.45822, p-value = 0.0002593
#DW стремится к 0, что говорит о положительной автокорреляции
#p-value = 0.0002593 < (0.01, 0.05, 0.1) - принимаем гипотезу о существовании автокоррелции

bgtest(p_many, order = 1, type = "F") # Тест Бреуша-Годфри, автокорреляция 1 порядка
bgtest(p_many, order = 2, type = "F") # Тест Бреуша-Годфри, автокорреляция 2 порядка
bgtest(p_many, order = 3, type = "F") # Тест Бреуша-Годфри, автокорреляция 3 порядка
#H0: нет автокорреляции
#Ha: есть автокорреляция n порядка
#LM test = 14.987, df1 = 1, df2 = 8, p-value = 0.004733
#LM test = 7.4288, df1 = 2, df2 = 7, p-value = 0.01859
#LM test = 4.9515, df1 = 3, df2 = 6, p-value = 0.0461

#pv = 0.004733 < (0.01, 0.05, 0.1) => H0 отвергается, автокорреляция 1 порядка присутствует
#(0.01) < pv = 0.01859 < (0.05, 0.1) => H0 отвергается, автокорреляция 2 порядка присутствует при 5% и 10%
#pv = (0.01) < pv = 0.0461 < (0.05, 0.1) => H0 отвергается, автокорреляция 3 порядка присутствует при 5% и 10%

#Вывод: проблема автокорреляции 1 порядка существует на всех уровнях значимости, автокорреляции 2 и 3 порядков существует на уровнях 5 и 10%

b <- coef(p_many)
# Средний лаг
b[2] * 0 + b[3] * 1 + b[4] * 2

# Краткосрочный мультипликатор
b[2]
# Долгосрочный мультипликатор
sum(b[2:length(b)])

#Проведите тест на длинную и короткую модель: сравните модель из условия с парной регрессией,
#описывающей зависимость текущего объёма спроса от текущего значения цены товара.
waldtest(lm(y ~ x0, data=train), p_many)

# Точечный прогноз
predict(p_many, newdata = test)
# Интервальный прогноз
predict(p_many, newdata = test, interval = "confidence")
predict(p_many, newdata = test, interval = "prediction")