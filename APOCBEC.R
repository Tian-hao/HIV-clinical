#R code
#caculate the apobec induced mutation
library(vegan)
DIV_THR = 0.1
png('../graph/APOBECMut.png',width=1600,height=1600)
sink('../graph/APOBECcount.txt')
par(mfrow=c(2,4))
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='../freq/freq',pattern=fullname)
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
        for (i in 2:5){
          count[,i] <- count[,i]+tmp[,i]
        }
      }
      flag <- matrix(,nrow=1520,ncol=3)
      flag[,1] <- c(1:1520)
      flag[,2:3] <- 0
      for (i in 1:1519){
        ref <- sort(count[i,2:5],decreasing=TRUE)
        ref2 <- sort(count[i+1,2:5],decreasing=TRUE)
        if (count[i,5]==ref[1] &&
	  (count[i+1,5]==ref2[1] || count[i+1,2]==ref2[1]) &&
	  count[i,2]==ref[2] && 
	  diversity(count[i,2:5])>DIV_THR){ flag[i,2] <- 1 }
        if (diversity(count[i,2:5])>DIV_THR){ flag[i,3] <- 1}
      }
      SWmatrix <- diversity(count[,2:5])
      pngfile <- paste('../graph/','G',g,'P',p,'T',t,'_APO.png',sep='')
      #png(pngfile)
      plot(count[,1],SWmatrix,xlim=c(0,1520),ylim=c(10e-3,1),xlab='position',ylab='SW Index',
        type='n',main=pngfile)
      cat(pngfile,sum(flag[,2]),sum(flag[,3]),'\n')
      for (i in 1:1520){
        if (flag[i,2]==0){
	  points(count[i,1],SWmatrix[i],col=2)
	}
	else{
	  points(count[i,1],SWmatrix[i],col=3)
	}
      }
      abline(h=DIV_THR,lwd=3,lty=2)
    }
  }
}


	  
	  
