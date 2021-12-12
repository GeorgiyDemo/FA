#install.packages("lmtest")
#install.packages("forecast")
#install.packages("tseries")
#install.packages("orcutt")
#install.packages("psych")
#install.packages("regclass")
library(orcutt)
library(lmtest)
library(forecast)
library(tseries)
library(orcutt)
library(psych)
library(regclass)
library(mctest)
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract17")

data <- read.csv('./data1.csv', sep = ";"); data
train <- data[1:29,]; train
test <- data[30:30,]; test

Q <- train$Q; Q
I <- train$I; I
M <- train$M; M
P <- train$P; P


p_many <- lm(Q~I+M+P)
s_many <- summary(p_many)
s_many

#Статистика
#R^2 = 0.8234058 - качество отличное
# Se = 0.450804 - качество хорошее
# Ош аппроксимации = 0.1630103 -  качество отличное
#Вывод: модель хороша 


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

#Оценка значимости:
  
#2e-16 < alfa --> отвергаем Н0 --> параметр значим
#4.81e-07 < alfa --> отвергаем Н0 --> параметр значим
#0.000257 < alfa --> отвергаем Н0 --> параметр значим
#0.051754 > alfa (0.01, 0.05) --> принимается Н0

#Экономическая интерпретация
#С ростом дохода на 1000 объем увеличится,
#вне зависимости ни от чего объем продаж (объем потребления) 166,6 млн

el1 <- s_many$coefficients[2] * mean(I) / mean(Q); el1
#0.1904783 -> не эластично
#I (с ростом дохода потребителей на 1% объем продаж увелич 0.1904783)
el2 <- s_many$coefficients[3] * mean(M) / mean(Q); el2
#0.01558067 -> не эластично
#M (с ростом дохода потребителей на 1% объем продаж увелич 0.01558067)
el3 <- s_many$coefficients[4] * mean(P) / mean(Q); el3
#-0.03635037 -> не эластично
#P (с ростом дохода потребителей на 1% объем продаж уменьшился 0.03635037)

#Анализ матриц парных корреляций;
cor(train)
corr.test(train, alpha=0.05)
#Самая сильная корреляция между I и M -> 0.78

#VIF – «фактор инфляции вариации»:
VIF(p_many)
#Т.к. коэффы < 2 --> мультиколлениарность отсутствует

#Тест Фаррара – Глоубера

imcdiag(p_many)
qchisq(0.95, 3*2)
# qchisq = 12.59159
#все значения wi < x2 табл, мультиколлинеарности нет
# факторы I и P имеют слабое влияние

############################################Посмотрение новых моделей с исключением факторов###############
#Выкидываем фактор P

m2 = lm(Q~I+M, data=train)
sm2 =summary(m2);sm2
AIC(m2)
#Все факторы значимы

m3 = lm(Q~M+P, data=train)
sm3 =summary(m3);sm3
AIC(m3)
#фактор P не значим


m4 = lm(Q~I+P, data=train)
sm4 =summary(m4);sm4
AIC(m4)
#Фактор P не значим

m5 = lm(Q~I, data=train)
sm5 =summary(m5);sm5
AIC(m5)
#Все факторы значимы

m6 = lm(Q~P, data=train)
sm6 =summary(m6);sm6
AIC(m6)
#Все факторы значимы

m7 = lm(Q~M, data=train)
sm7 =summary(m7);sm7
AIC(m7)
#Все факторы значимы

#################################Выводы по устанениям мулькиколлинеарности с помощью AIC###############################
#Лучше всего использовать модель с факторами  Q~I+M (AIC = 44.26091)

test
predict(p_many, newdata = test, interval = "confidence", level = 0.95);
predict(p_many, newdata = test, interval = "prediction", level = 0.95);
#yреал_30=201.65; yреал_30 принадлежит (201.3126;202.0529) - доверительный
#yреал_30=201.65; yреал_30 принадлежит (200.6833;202.6823) - предиктивный
#Модель адекватна двум интервалам
