library(forecast)
library(lmtest)
require(readxl)
library(orcutt)
library(sandwich)
library(car)

# Получение данных
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract19")
data <- read.csv('./data.csv', sep = ";"); data

y <- data$y
y
x <- data$x
x
t1 <- data$t1
t1
t2 <- data$t2
t2

p_many <- lm(y ~ x + t1 + t2, data = data[1:13, ]);p_many
s_many <- summary(p_many);s_many


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

c <- data[14, ];c

predict(p_many, newdata = c, interval = 'confidence')
predict(p_many, newdata = c, interval = 'prediction')

cor(data[1:13, ])

dwtest(p_many)
gqtest(p_many) # Голдфельд-Квандт
bptest(p_many, studentize = TRUE) # Бреуша-Пагана
bgtest(p_many, order = 1, order.by = NULL, type = c("Chisq", "F")) # Бреуш-Годфри

kratk = s_many$coefficients[2];kratk
dolg = sum(s_many$coefficients[2]+s_many$coefficients[3]+s_many$coefficients[4]);dolg
avgm = s_many$coefficients[3]*1 +s_many$coefficients[4]*2;avgm

m1 <- lm(y ~ x, data = data[1:13, ]);m1
sm1 <- summary(m1);sm1

waldtest(p_many,m1, test='F')

pred<-data.frame(c(205),c(132),c(135))
colnames(pred)<-c("x","t1","t2")
pred
predictY<-predict(p_many,newdata = pred, interval = 'confidence');predictY
predictY<-predict(p_many,newdata = pred, interval = 'prediction');predictY


