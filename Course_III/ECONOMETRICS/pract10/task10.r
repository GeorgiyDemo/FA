#install.packages("lmtest")
#install.packages("tseries")
#install.packages("forecast")
library(lmtest)
library(forecast)
library(tseries)

setwd("/Users/demg/Documents/Projects/FA/Course\ III/ECONOMETRICS/pract10")
data <- read.csv("./data10.csv", sep = ';',header = TRUE)
data

y=data$Y; y
x=data$X; x
pm <- lm(y~x); pm

vcov(pm)
