#R code
#rank correlation of diversity
#install.packages("vegan")
library(vegan)
png('../graph/correlationDiversity.png',width=1800,height=1200)
par(mfrow=c(2,4))
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    fullname <- paste('G',g,'P',p,'T1.*.count',sep='')
    patientfiles <- list.files(path='../freq/freq',pattern=fullname)
    shortname <- paste('G',g,'P',p,sep='')
    pngfile <- paste('../graph/',shortname,'.png',sep='')
    count1 <- matrix(,nrow=1520,ncol=5)
    count1[,1] <- c(1:1520)
    count1[,2:5] <- 0
    for (filename in patientfiles){
      tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
      for (i in 2:5){
	count1[,i] <- count1[,i]+tmp[,i]
      }
    }
    fullname <- paste('G',g,'P',p,'T2.*.count',sep='')
    patientfiles <- list.files(path='../freq/freq',pattern=fullname)
    shortname <- paste('G',g,'P',p,sep='')
    pngfile <- paste('../graph/',shortname,'.png',sep='')
    count2 <- matrix(,nrow=1520,ncol=5)
    count2[,1] <- c(1:1520)
    count2[,2:5] <- 0
    for (filename in patientfiles){
      tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
      for (i in 2:5){
	count2[,i] <- count2[,i]+tmp[,i]
      }
    }
    ddd1 <- diversity(count1[,2:5])
    ddd2 <- diversity(count2[,2:5])
    plot(rank(ddd1),rank(ddd2),xlim=c(1,1520),ylim=c(1,1520),xlab='Time 1',ylab='Time2',
      main=shortname,col=2)
    spear <- cor(ddd1,ddd2,method='spearman')
    legend('topleft',paste('r=',spear,sep=''))
  }
}  





