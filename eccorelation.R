#Rcode
#correlation before and after error correction

ec1 <- read.table("ecresult/G2P1T1.count",header=F)
ec5 <- read.table("ecresult/G2P5T1.count",header=F)
p1files <- list.files(path='./freq/',pattern='G2P1T1.*.count')
count1 <- matrix(,nrow=1520,ncol=5)
count1[,1] <- c(1:1520)
count1[,2:5] <- 0
for (filename in p1files){
  tmpfile <- paste('./freq/',filename,sep='')
  tmp <- read.table(tmpfile,header=F)
  for (i in 2:5){
    count1[,i] <- count1[,i]+tmp[,i]
  }
}
p5files <- list.files(path='./freq/',pattern='G2P5T1.*.count')
count5 <- matrix(,nrow=1520,ncol=5)
count5[,1] <- c(1:1520)
count5[,2:5] <- 0
for (filename in p5files){
  tmpfile <- paste('./freq/',filename,sep='')
  tmp <- read.table(tmpfile,header=F)
  for (i in 2:5){
    count5[,i] <- count5[,i]+tmp[,i]
  }
}
for (row in 1:1520){
  total <- 0
  for (col in 2:5){
    total <- total + count1[row,col]
  }
  for (col in 2:5){
    count1[row,col] <- count1[row,col]/total
  }
}
for (row in 1:1520){
  total <- 0
  for (col in 2:5){
    total <- total + count5[row,col]
  }
  for (col in 2:5){
    count5[row,col] <- count5[row,col]/total
  }
}
for (row in 1:1520){
  total <- 0
  for (col in 2:5){
    total <- total + ec1[row,col]
  }
  for (col in 2:5){
    ec1[row,col] <- ec1[row,col]/total
  }
}
for (row in 1:1520){
  total <- 0
  for (col in 2:5){
    total <- total + ec5[row,col]
  }
  for (col in 2:5){
    ec5[row,col] <- ec5[row,col]/total
  }
}
png('eccorrelation.png',height=900,width=900)
par(mfrow=c(2,2))
plot(count1[,2],ec1[,2],type='n',main='patient1',xlab='pre-correction',ylab='post-correction',
  xlim=c(0,1),ylim=c(0,1))
for (i in 2:5){
  points(count1[,i],ec1[,i],col=i)
}
plot(count1[,2],ec1[,2],type='n',main='patient5',xlab='pre-correction',ylab='post-correction',
  xlim=c(0,1),ylim=c(0,1))
for (i in 2:5){
  points(count5[,i],ec5[,i],col=i)
}
plot(count1[,2],ec1[,2],type='n',main='p1-post5',xlab='pre-correction',ylab='post-correction',
  xlim=c(0,1),ylim=c(0,1))
for (i in 2:5){
  points(count1[,i],ec5[,i],col=i)
}
plot(count1[,2],ec1[,2],type='n',main='p5-post1',xlab='pre-correction',ylab='post-correction',
  xlim=c(0,1),ylim=c(0,1))
for (i in 2:5){
  points(count5[,i],ec1[,i],col=i)
}
