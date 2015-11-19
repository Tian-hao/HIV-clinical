#R code
png('dnds.png',res=200,width=1800,height=1800)
par(mfrow=c(1,2))
a1 <- read.table('dnds/G1P1T2.ph.fubar.csv',header=T,sep=',')
a11 <- a1[,3]/a1[,2]
plot(a11,log='y',main='G1P1T2',ylab='dN/dS',xlab='position',ylim=c(0.02,20))
a2 <- read.table('dnds/G2P1T2.ph.fubar.csv',header=T,sep=',')
a22 <- a2[,3]/a2[,2]
plot(a22,log='y',main='G2P1T2',ylab='dN/dS',xlab='position',ylim=c(0.02,20))


