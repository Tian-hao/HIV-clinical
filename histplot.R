#R code
#pilot run to visualize data

a <- read.table("../freq/G1P1T1.freq",header=T)
png("../plot/hist1.png")
plot(a[,1],a[,2],col=1)
points(a[,1],a[,3],col=2)
points(a[,1],a[,4],col=3)
points(a[,1],a[,5],col=4)
