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
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract12")

data <- read.csv('./task3.csv', sep = ";")
x <- data$Цена; x
y <- data$Площадь; y


# Парная модель
p_many <- lm(x~y)
s_many <- summary(p_many)
s_many

# Корреляционная матрица
cor(data) 

# Диаграммы рассеяния
plot(y, x, col = 'red')


# Доверительный интервал
confint(p_many, level = 0.95)

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
#Вывод о качестве: модель приемлима, R2 не идеален


gqtest(p_many, order.by = x, fraction = 0.25) # Тест Голдфельда-Квандта для x
#GQ < Fтаб – Гомоскедастичность – H0<br>
#GQ > Fтаб – Гетероскедастичность - Hа<br>
#GQ = 84.341, df1 = 6, df2 = 5, p-value = 7.353e-05
#alternative hypothesis: variance increases from segment 1 to 2<br>
#p-value = 7.353e-05 < (0.1; 0.05; 0.01), присутствует проблема гетероскедастичности<br>


bptest(p_many, studentize = TRUE) # Тест Бреуша-Пагана
#Гомоскедастичность – H0<br>
#Гетероскедастичность - Hа<br>
#BP = 0.74029, df = 1, p-value = 0.389
#p-value = 0.389 > (0.1; 0.05; 0.01), отсутствует проблема гетероскедастичности<br>


dw <- dwtest(p_many); dw # Тест Дарбина-Ватсона
#H0: нет автокорреляции<br>
#Ha: есть автокорреляция 1-го порядка<br>
#DW = 2.251, p-value = 0.6685
#DW не стремится к 0, что говорит об отсутствии положительной автокорреляции
#p-value = 0.6685 > (0.01, 0.05, 0.1) - принимаем гипотезу об отсутствии автокорреляции, отвергаем гипотезу о существовании автокоррелции


bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
bgtest(p_many, order = 2, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
bgtest(p_many, order = 3, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0: нет автокорреляции
#Ha: есть автокорреляция n порядка
#LM test = 0.5256, df = 1, p-value = 0.4685
#LM test = 1.6217, df = 2, p-value = 0.4445
#LM test = 3.518, df = 3, p-value = 0.3184

#LM test = 25.304, df = 3, p-value = 0.03291<br>
#pv = 0.4685 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 1 порядка отсутствует<br>
#pv = 0.4445 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 2 порядка отсутствует<br>
#pv = 0.3184 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 3 порядка отсутствует<br>

#############################################Устраняем проблему гетероскедастичности#################################

y3<-y/predict(p_many)
x3<-x/predict(p_many)
m3<-lm(y3~x3)
s3<-summary(m3)
s3

gqtest(m3, order.by = x3, fraction = 0.25) # Тест Голдфельда-Квандта для x3
#GQ < Fтаб – Гомоскедастичность – H0
#GQ > Fтаб – Гетероскедастичность - Hа
#GQ = 0.30083, df1 = 6, df2 = 5, p-value = 0.9121
#alternative hypothesis: variance increases from segment 1 to 2<br>
#p-value = 0.9121 > (0.1; 0.05; 0.01), отсутствует проблема гетероскедастичности


bptest(m3, studentize = TRUE) # Тест Бреуша-Пагана
#Гомоскедастичность – H0
#Гетероскедастичность - Hа
#BP = 2.024, df = 1, p-value = 0.1548
#p-value = 0.1548 > (0.1; 0.05; 0.01), отсутствует проблема гетероскедастичности

#######################################################################################################################################