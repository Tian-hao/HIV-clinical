#R code
#correlation between T1 and T2
library("RColorBrewer")
png('../graph/corelationT12.png',res=400,width=4000,height=2000)
par(mfrow=c(2,4))
par(cex=0.6)
par(mar = c(0, 0, 0, 0), oma = c(4, 4, 0.5, 0.5))
par(tcl = -0.25)
par(mgp = c(2, 0.6, 0))
mycol = brewer.pal(4,'Set3')
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
    fullname <- paste('G',g,'P',p,sep='')
    plot(freq1[,2],freq2[,2],type='n',pch='.',axes = FALSE,
      xlim=c(10e-5,1),ylim=c(10e-5,1),log='xy')
    for (i in 2:5){
      points(freq1[,i],freq2[,i],col=mycol[i-1])
    if (g==2 & p %in% c(1,3)) axis(1,at=exp(seq(log(1e-4), log(1), length.out = log(10))))
    if (p==1 & g==2) axis(2,at=exp(seq(log(1e-4), log(1), length.out = log(10))))
    if (g==2 & p==5) legend('bottomright',c('A','T','C','G'),pch=1,col=mycol)
    box()
    mtext(fullname,side=3,line=-1,adj=0.1,cex=0.6)
    }
  }
}
mtext("Timepoint 1", side = 1, outer = TRUE, cex = 0.7, line = 2.2)
mtext("Timepoint 2", side = 2, outer = TRUE, cex = 0.7, line = 2.2)
