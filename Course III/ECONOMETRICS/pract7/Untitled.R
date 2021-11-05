"""
Задача 2. 
А) Постройте линейную модель регрессии, описывающую зависимость между затратами на рекламу и количеством туристов, обратившихся в туристическую фирму. 
Б) Построите 90%-й доверительный интервал для коэффициентов модели. 
В) Проверьте значимость модели регрессии в целом и каждого коэффициента модели по отдельности.
Г) Сделайте выводы о качестве модели.
Д) Проверьте выполнение предпосылки о гомоскедастичности с помощью:
- теста Гольдфельда-Квандта;
- теста Бройша-Пагана.
Е) Проверьте выполнение предпосылки об отсутствии автокорреляции остатков с помощью:
- теста Дарбина-Уотсона;
- теста Бройша-Годфри.

Файл с исходными данными задачи – task2.txt, где в столбце Reclama приведены затраты на рекламу (в тыс. у.е.), а в столбце Turist – количество туристов, обратившихся за услугами.

"""

library(lmtest)
library(binom)
require(readxl)

setwd('/Users/demg/Projects/FA/Course III/ECONOMETRICS/task7')
data <- read.table('task2.txt',  header=TRUE)
y <- data$Reclama
x1 <- data$Turist

lm <- lm(y ~ x1)
slm <- summary(lm)

t_table2 <- qt(0.9, df = slm$fstatistic[["dendf"]])
B <- slm$coefficients[, 1]
di_lower <- B - slm$coefficients[, 2] * t_table2
di_upper <- B + slm$coefficients[, 2] * t_table2

#Fisher-test
F_statistic_p <- slm$fstatistic["value"][[1]]
F_table_p <- 3.55
F_statistic_p < F_table_p # Модель в целом значима

# t-критерий Стьюдента для оценки значимости параметров модели линейной регрессии
t2 <- slm$coefficients[, 1] / slm$coefficients[, 2]
t_table2 <- qt(0.975, df = slm$fstatistic[["dendf"]])
t2 < t_table2 # Все коэфы незначимы

slm_r_squared <- slm$r.squared
slm_r_squared
slm_std_error <- slm$sigma
slm_std_error
slm_approx_error <- sum(abs(slm$residuals/y)) / length(y) * 100
slm_approx_error

dw <- dwtest(lm)

bg <- bgtest(lm, order = 1, order.by = NULL, type = c("Chisq", "F"))
qchisq(p = 0.95, df = 2)

gq <- gqtest(lm, order.by = x1, fraction = 0.05)
gq
bp <- bptest(lm, studentize = TRUE)
bp
