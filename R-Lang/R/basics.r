


# Working on Data import 

# numbers = scan()
# characters = scan(what =  "character")
# library(data.table)
# mydata = fread("test.csv")
# mydata
# summary(mydata$`20 -30g`)


# x = 5:7
# y = 8:10
# plot(x,y)
# install.packages(lynx)
# 
# plot(lynx)
# 
# # Title color , title , color, title magnification
# 
# plot(lynx, main="Lynx Trappings",col="red",col.main=52,cex.main=1.5)
# plot(lynx, ylab="Lynx Trapping",xlab="Time value",las=2)

# x = matrix(c(1:9),nr=3,byrow =T)
# print(x)
# apply(x,1,mean)
# apply(x,2,mean)
# apply(x,1,plot)
# 
library(ggplot2)
head(diamonds)
attach(diamonds)

qqnorm(depth)
hist(depth)
depthsmall = sample(depth, 5000)

shapiro.test(depthsmall)

library(nortest)
cvm.test(depth)
lillie.test(depth)
sf.test(depthsmall)
pearson.test(depth)



