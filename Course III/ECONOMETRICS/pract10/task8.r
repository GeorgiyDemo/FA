#install.packages("lmtest")
#install.packages("forecast")
#install.packages("tseries")
#install.packages("orcutt")

library(lmtest)
library(forecast)
library(tseries)
library(orcutt)
setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract10")

data <- read.csv("./data8.csv", sep = ';',header = TRUE)
data

y <- data$Y; y
x1 <- data$X1; x1
x2 <- data$X2; x2
pm <- lm(y~x1+x2); pm

cochrane.orcutt(pm)