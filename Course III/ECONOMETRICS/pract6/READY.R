# install.packages('lmtest')
# install.packages('car')
library(lmtest)
library(car)

setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task6')
data <- read.table('./Demenchuk.txt',  header=TRUE)
data

y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3

# Корреляционная матрица
cor(data) 

# Диаграммы рассеяния
plot(y, x1, col = 'red')
plot(y, x2, col= 'blue')
plot(y, x3, col = 'green')

########################################################################################
# Множественная модель
p_many <- lm(y~x1+x2+x3)
s_many <- summary(p_many)
s_many

A_many <- sum(abs(s_many$residuals/y)) / length(y) * 100 # Апроксимация
A_many

confint(p_many, level = 0.95) # Доверительные интервалы


beta_many_1 <- s_many$coefficients[2] # Бета коэффициент для x1
beta_many_1

delta_many_1 <- cor(y, x1) * beta_many_1 / s_many$r.squared # Дельта коэффициент для x1
delta_many_1
elastic_many_1 <- beta_many_1 * mean(x1) / mean(y) # Коэффициент эластичности для x1
elastic_many_1

beta_many_2 <- -s_many$coefficients[3] # Бета коэффициент для x2
beta_many_2
delta_many_2 <- cor(y, x2) * beta_many_2 / s_many$r.squared # Дельта коэффициент для x2
delta_many_2
elastic_many_2 <- beta_many_2 * mean(x2) / mean(y) # Коэффициент эластичности для x2
elastic_many_2

beta_many_3 <- -s_many$coefficients[4] # Бета коэффициент для x3
beta_many_3
delta_many_3 <- cor(y, x3) * beta_many_3 / s_many$r.squared  # Дельта коэффициент для x3
delta_many_3
elastic_many_3 <- beta_many_3 * mean(x3) / mean(y) # Коэффициент эластичности для x3
elastic_many_3


dwtest(p_many) # Тест Дарбина-Ватсона
bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
gqtest(p_many, order.by = x1, fraction = 0.25) # Тест Голдфельда-Квандта для x1
bptest(p_many, studentize = TRUE) # Тест Бреуша-Пагана

###################################################################################################
# Парная модель
p_pair <- lm(y~x1)
s_pair <- summary(p_pair)
s_pair

A_pair <- sum(abs(s_pair$residuals/y)) / length(y) * 100 # Апроксимация
A_pair

confint(p_pair, level = 0.95) # Доверительные интервалы

beta_pair <- s_pair$coefficients[2] # Бета коэффициент для x1
beta_pair
delta_pair <- cor(y, x1) * beta_pair / s_pair$r.squared # Дельта коэффициент для x1
delta_pair
elastic_pair <- beta_pair * mean(x1) / mean(y) # Коэффициент эластичности для x1
elastic_pair


dwtest(p_pair) # Тест Дарбина-Ватсона
bgtest(p_pair, order = 1, order.by = NULL, type = c("Chisq", "F")) # Тест Бреуша-Годфри
gqtest(p_pair, order.by = x1, fraction = 0.25) # Тест Голдфельда-Квандта для x1
bptest(p_pair, studentize = TRUE) # Тест Бреуша-Пагана
####################################################################################################
error_pair <- sqrt(deviance(p_pair)/df.residual(p_pair))
error_many <- sqrt(deviance(p_many)/df.residual(p_many))

# Сравнение моделей
determ <- c(s_pair$r.squared , s_many$r.squared)
adjust_determ <- c(s_pair$adj.r.squared, s_many$adj.r.squared)
st_error <- c(error_pair, error_many)
print(st_error)
approx <- c(A_pair, A_many)
f_test <- c(s_pair$fstatistic[1], s_many$fstatistic[1])

compare <- data.frame(
  Коэффициент_детерминации=determ,
  Скорректированный_коэффициент=adjust_determ,
  Стандартная_ошибка_модели=st_error,
  Ошибка_аппроксимации=approx,
  F_тест=f_test
)

#Аппроксимация: меньше - лучше
#Стандартная ошибка: меньше- лучше
# Determinate: больше - лучше
# Adjust_determinate: больше - лучше
# F_test: больше - лучше


 #1 - парная
 #2 - множествееная
compare <- rbind(compare, list("Множественная модель", "Множественная модель", "Множественная модель", "Множественная модель", "Парная модель"))
compare
# Выигрывает множественная модель по 4 из 5 пунктов