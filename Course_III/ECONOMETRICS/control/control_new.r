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
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/control")
data <- read.csv('./control.csv', sep = ","); data

y <- data$y; y
x1 <- data$x1; x1
x2 <- data$x2; x2

p_many <- lm(y~x1+x2)
s_many <- summary(p_many)
s_many

round(s_many$coefficients[7],3)
round(s_many$coefficients[9],3)

f_table = round(qf(0.95, 2, 150-2-1),3);f_table

determ <- round(s_many$r.squared, 3)
adjust_determ <- round(s_many$adj.r.squared, 3)
st_error <- round(sqrt(deviance(p_many)/df.residual(p_many)), 3)
approx <- round(sum(abs(s_many$residuals/y)) / length(y) * 100, 3)
f_test <- round(s_many$fstatistic[1], 3)

compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)
print(compare)

#######################бета-коэффициенты, дельта-коэффициент, коэффы элластичностиы##########################################

beta_pair1 <- s_many$coefficients[2] # Бета коэффициент для x1
round(beta_pair1,3)
delta_pair1 <- cor(y, x1) * beta_pair1 / s_many$r.squared # Дельта коэффициент для x1
round(delta_pair1,3)
elastic_pair1 <- beta_pair1 * mean(x1) / mean(y) # Коэффициент эластичности для x1
round(elastic_pair1,3)

beta_pair2 <- s_many$coefficients[3] # Бета коэффициент для x2
round(beta_pair2,3)
delta_pair2 <- cor(y, x2) * beta_pair2 / s_many$r.squared # Дельта коэффициент для x2
round(delta_pair2,3)
elastic_pair2 <- beta_pair2 * mean(x2) / mean(y) # Коэффициент эластичности для x2
round(elastic_pair2,3)

####################################Тест на длинную/короткую модель##################################
p4 <- lm(y~x2)
s4 <- summary(p4); s4

#Проводим тест вальда
wald_test <- waldtest(p_many, p4, test="F")


round(wald_test$F[2], 3) # F
round(wald_test$`Pr(>F)`[2],3) # p-value

#H0: короткая модель
#Н1: длинная модель
#Fнабл > Fкр(0.01, 0.05, 0.1), h1, короткая модель
#Fнабл < Fкр(0.01, 0.05, 0.1), h1, длинная модель

corr <- cor(data)
t_nabl <- sqrt(corr*corr/(1-corr*corr)*(150-2)); t_nabl
t_tabl <- qt(0.05, 150-2); t_tabl

#############################Нормальность остатков######################################################## (?)
#проверяем остатки на нормальность
ost = s_many$residuals
ost

jarque.bera.test(ost)
#h0- остатки нормально распределены
#h1-остатки ненормально распределены
#P-val=0.9 > alpha; h0 принимаем, остатки норм распределены

#Корреляция
cor(data)
corr.test(data, alpha=0.05)
##################################ПРОВЕРКА НА ГЕТЕРОСКЕДАСТИЧНОСТЬ##################################

gqtestresults <- gqtest(p_many, order.by = y) # Тест Голдфельда-Квандта для y
gqtestresults
round(gqtestresults$statistic[1],3)
round(gqtestresults$p.value,3)

#GQ = 1, df1 = 54, df2 = 53, p-value = 0.5
#p value = 0.348 - это гетеро или гомо?

#alternative hypothesis: variance increases from segment 1 to 2
#p-value = 0.348 > (0.1; 0.05; 0.01), нет проблемы гетероскедастичности


resultbptest <- bptest(p_many, studentize = TRUE) # Тест Бреуша-Пагана (Тест Уайта)
resultbptest
round(resultbptest$statistic,3)
round(resultbptest$p.value,3)

resultbptest$parameter
#Гомоскедастичность – H0
#Гетероскедастичность - Hа
#BP = 0.32, df = 2, p-value = 0.9
#p-value = 0.852 > (0.1; 0.05; 0.01), отсутствует проблема гетероскедастичности
#ВЫВОД: Нет проблем гетероскедастичности

##################################ПРОВЕРКА НА АВТОКОРРЕЛЯЦИЮ#######################################


dw <- dwtest(p_many); dw # Тест Дарбина-Ватсона
round(dw$statistic[1],3)
#H0: нет автокорреляции
#Ha: есть автокорреляция 1-го порядка
#DW = 2, p-value = 0.6
#DW не стремится к 0, что говорит об отсутствии положительной автокорреляции
#p-value = 0.6 > (0.01, 0.05, 0.1) - принимаем гипотезу об отсутствии автокорреляции, отвергаем гипотезу о существовании автокоррелции

bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
bgtest(p_many, order = 2, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
bgtest(p_many, order = 3, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
#H0: нет автокорреляции
#Ha: есть автокорреляция n порядка
#LM test = 0.029, df = 1, p-value = 0.9
#LM test = 0.094, df = 2, p-value = 1
#LM test = 0.46, df = 3, p-value = 0.9

#pv = 0.9 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 1 порядка отсутствует
#pv = 1 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 2 порядка отсутствует
#pv = 0.9 > (0.01, 0.05, 0.1) => H0 принимается, автокорреляция 3 порядка отсутствует

#Вывод: проблема автокорреляции отсутствует

####################################################Мультиколлинеарность################################################
result <- VIF(p_many)
round(result[1],3)
round(result[2],3)
#VIF < 2 - ничего нет

