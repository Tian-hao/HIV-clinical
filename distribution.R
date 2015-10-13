#R code
#distribution of four kinds of mutations' frequency
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
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
      freq <- matrix(,nrow=1520,ncol=5)
      freq[,1] <- c(1:1520)
      freq[,2:5] <- 0
      for (row in 1:1520){
        total <- count[row,2]+count[row,3]+count[row,4]+count[row,5]
	for (col in 2:5){
	  freq[row,col] <- count[row,col]/total
	}
      }
      picname <- paste('graph/',fullname,'.distribution0.png')
      png(picname)
      breaks=exp(seq(log(10e-5),log(0.05),5))
      hist(freq[,2],breaks=breaks,xlim=c(10e-5,0.05),ylim=c(0,1),log='x',freq=FALSE)
      hist(freq[,3],breaks=breaks,add=T)
      hist(freq[,4],breaks=breaks,add=T)
      hist(freq[,4],breaks=breaks,add=T)
    }
  }
}

