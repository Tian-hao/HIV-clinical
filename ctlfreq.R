#Rcode
library(RColorBrewer)
png('ctlfreq.png',res=200,width=1800,height=1800)
par(mfrow=c(1,2))
mycol <- brewer.pal(4,'YlOrRd')
a1 <- read.table('ctl.freq',header=F)
newdata <- a1[order(-a1[,2]),] 
plot(newdata[,2],type='h',col=mycol[newdata[,3]],
  xlab='haplotypes',ylab='frequency',lwd=3,main='Fast progressor')
legend('topright',col=mycol,legend=c('0.25','0.50','0.75','1.00'),pch=1)
a1 <- read.table('ctl.freq2',header=F)
newdata <- a1[order(-a1[,2]),]
plot(newdata[,2],type='h',col=mycol[newdata[,3]],
  xlab='haplotypes',ylab='frequency',lwd=6,main='Elite controller')

