#R code

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
      cover <- matrix(,nrow=1520,ncol=2)
      cover[,1] <- c(1:1520)
      cover[,2] <- 0
      for (i in 2:5){
        cover[,2] <- cover[,2]+count[,i]
      }
      picname <- paste('graph/',fullname,'.png')
      png(picname)
      plot(cover[,1],cover[,2],main=fullname,xlab='residue',ylab='count')
    }
  }
}

