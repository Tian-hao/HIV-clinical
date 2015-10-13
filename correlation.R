#R code
#correlation between T1 and T2
for (g in 1:2){
  for (p in 1:5){
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='.',pattern=fullname)
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(filename,header=F)
	for (i in 2:5){
	  count[,i] <- count[,i]+tmp[,i]
	}
      }
      if (t==1){
        freq1 <- matrix(,nrow=1520,ncol=5)
        freq1[,1] <- c(1:1520)
        freq1[,2:5] <- 0
        for (row in 1:1520){
          total <- count[row,2]+count[row,3]+count[row,4]+count[row,5]
	  for (col in 2:5){
	    freq1[row,col] <- count[row,col]/total
	  }
	}
      }
      if (t==2){
        freq2 <- matrix(,nrow=1520,ncol=5)
        freq2[,1] <- c(1:1520)
        freq2[,2:5] <- 0
        for (row in 1:1520){
          total <- count[row,2]+count[row,3]+count[row,4]+count[row,5]
          for (col in 2:5){
	    freq2[row,col] <- count[row,col]/total
	  }
	}
      }
    }
    picname <- paste('graph/',fullname,'.logfreq.png')
    png(picname)
    plot(freq1[,2],freq2[,2],type='n',main=fullname,xlab='Time1',ylab='Time2',
      xlim=c(10e-5,1),ylim=c(10e-5,1),log='xy')
    for (i in 2:5){
      points(freq1[,i],freq2[,i],col=i)
    }
  }
}

