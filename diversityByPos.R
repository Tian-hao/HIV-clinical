#R code
#mutation diversity of each sample, linear adding SW-index at every position
#install.packages("vegan")
library(vegan)
png('../graph/diversitybypos.png',width=1800,height=1200)
par(mfrow=c(2,4))
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='../freq/freq',pattern=fullname)
      shortname <- paste('G',g,'P',p,sep='')
      pngfile <- paste('../graph/',shortname,'.png',sep='')
      #if (t==1){
      #  png(pngfile)
      #}
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
	for (i in 2:5){
	  count[,i] <- count[,i]+tmp[,i]
	}
      }
      SWmatrix <- diversity(count[,2:5])
      if (t==1){
        plot(count[,1],SWmatrix,xlim=c(0,1520),ylim=c(10e-3,1),xlab='position',ylab='SW Index',
          main=shortname,col=2,log='y')
      }
      if (t==2){
        points(count[,1],SWmatrix,col=3)
      }
    }
  }
}  





