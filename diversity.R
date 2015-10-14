#R code
#mutation diversity of each sample, linear adding SW-index at every position
#install.packages("vegan")
library(vegan)
SWmatrix <- vector(,length=16)
sink('../graph/diversity.txt')
png('../graph/diversity.png')
plot(c(1),type='n',xlim=c(0,17),ylim=c(0,200),xlab='samples',ylab='SW Index',
  main='Diveristy',xaxt='n')
axis(1,lables='from G1P1T1 to G2P5T2')
flag <- 0
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      flag <- flag+1
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='../freq/freq',pattern=fullname)
      SWindex <- 0
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
	for (i in 2:5){
	  count[,i] <- count[,i]+tmp[,i]
	}
      }
      for (row in 1:1520){
        SWindex <- SWindex+diversity(count[row,2:5])
      }
      SWmatrix[flag] <- SWindex
      points(flag,SWmatrix[flag],type='h')
      cat(fullname,SWindex,'\n',sep='')
    }
  }
}  





