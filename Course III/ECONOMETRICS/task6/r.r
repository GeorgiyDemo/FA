setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task6')
data <- read.table('./Demenchuk.txt',  header=TRUE)

getwd()
#install.packages('lmtest')
library(lmtest)

print(data)
y <- data$y
x1 <- data$x1
x2 <- data$x2
x3 <- data$x3

#линейная модель 
m<-lm(y ~ x1 + x2 + x3, data = data)
m
sm<-summary(m)
sm
A1 <- (sum(abs(sm$residuals/y))/length(y))*100

print(sm1$sigma)
print(sm1$r.squared)
print(sm1$fstatistic)
print(A1)

sm = summary(m);sm
e=sm$residuals;e


#GQtest
gq = gqtest(m, order.by= ~y, fraction=0, data=data);gq
# pv<a => присутствует проблема гетероскедастичности

#BPtest
bp = bptest(m, data=data);bp
# pv<a => присутствует проблема гетероскедастичности

#DWtest
dw = dwtest(m);dw
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

#BGtest
bg = bgtest(m,order = 1);bg
bgF = bgtest(m,order = 1,type = "F");bgF
# pv>a => H0 принимается, автокорреляция первого порядка отсутствует

e2 = e^2
plot(data$x1, e2)
plot(data$x2, e2)
plot(data$x3, e2)