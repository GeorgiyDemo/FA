#ПИ19-3 Деменчук Георгий ДЗ 3
#install.packages('lmtest')
library(lmtest)

data <- read.csv(file = '/Users/demg/Projects/FA/Course III/ECONOMETRICS/task3/data.csv', sep = ";")
data
y = data$Объем.денежных.накоплений.в.РФ.миллиард.руб...y.
x1 <- data$Сводные.данные.о.продаже.наличной.иностранной.валюты.кредитными.организациями.физическим.лицам..x1.
x2 <- data$Курс.рубля.к.доллару.США..x2.
x3 <- data$Цена.нефти.марки..Юралс...x3.
x4 <- data$Динамика.потребительских.цен.по.группам.товаров.и.услуг..месяц.к.соответствующему.месяцу.предыдущего.года......x4.

model <- lm(y ~ x1 + x2 + x3 +x4, data = data)
summary(model)

summary(model)$coefficient

confint(model)

