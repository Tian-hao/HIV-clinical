#R code
#mutation rate distribution by locus
png('../graph/distributionByPos.png',width=1800,height=1800)
par(mfrow=c(4,4))
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='../freq/freq/',pattern=fullname)
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
	for (i in 2:5){
	  count[,i] <- count[,i]+tmp[,i]
	}
      }
      freq <- matrix(,nrow=1520,ncol=5)
      freq[,1] <- c(1:1520)
      freq[,2:5] <- 0
      for (row in 1:1520){
        total <- count[row,2]+count[row,3]+count[row,4]+count[row,5]
	for (col in 2:5){
	  freq[row,col] <- count[row,col]/total
	  if (total==0) freq[row,col] <- 0
	  if (freq[row,col]>0.5){
	    freq[row,col] <- 0
	  }
	}
      }
      picname <- paste('../graph/G',g,'P',p,'T',t,'dist.png',sep='')
      #png(picname)
      plot(freq[,1],freq[,2],type='n',main=picname,xlab='position',ylab='freq',
        xlim=c(0,1520),ylim=c(10e-5,1),log='y')
      for (col in 2:5){
        points(freq[,1],freq[,col],col=col)
      }
    }
  }
}

