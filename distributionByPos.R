#R code
#mutation rate distribution by locus
library("RColorBrewer")
png('../graph/distributionByPos.png',res=250,width=1800,height=1800)
par(mfrow=c(4,4))
par(cex=0.6)
par(mar = c(0, 0, 0, 0), oma = c(4, 4, 0.5, 0.5))
par(tcl = -0.25)
par(mgp = c(2, 0.6, 0))
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
#	  if (freq[row,col]>0.5){
#	    freq[row,col] <- 0
#	  }
	}
      }
      picname <- paste('G',g,'P',p,'T',t,sep='')
      #png(picname)
      plot(freq[,1],freq[,2],type='n',axes = FALSE,
        xlim=c(0,1520),ylim=c(1e-4,1),log='y')
      mtext(picname,side=3,line=-1,adj=0.1,cex=0.6)
      if ((g==2) & (p %in% c(3,5)) & (t==1)) axis(1,at=seq(0,1500,500))
      if ((t==1) & (p ==1)) axis(2,at=exp(seq(log(1e-4), log(1), length.out = log(10))))
      box()
      col = brewer.pal(4,'Set3')
      for (i in 2:5){
        points(freq[,1],freq[,i],col=col[i-1],pch='.')
      }
    }
  }
}
mtext("residue", side = 1, outer = TRUE, cex = 0.7, line = 2.2)
mtext("frequency", side = 2, outer = TRUE, cex = 0.7, line = 2.2)
