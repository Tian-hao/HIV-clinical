#R code
#summarize the tests for manuscripts

#depth, raw/ mapping/ filtering
a1 <- read.table('../logs/readcountraw.log',sep=' ')
long <- length(a1[,1])
sink('../logs/raw.dep')
patient <- list()
for (i in 1:long){
  pt <- substr(a1[i,2],1,6)
  if (grepl('bc',a1[i,2])) next
  read <- a1[i,1]
  if (!(pt %in% patient)){
    patient <- list(patient,pt)
    cat(pt)
    cat('\t')
    cat(read)
    cat('\n')
  }
}
sink()

a1 <- file('../logs/readcountmap.log','r')
line <- readLines(a1)
long <- length(line)
patient <- ''
count <- 0
sink('../logs/mapping.dep')
for (i in 1:long){
  if (i %% 3 == 1){
    pt <- substr(line[i],20,25)
  }
  if (i %% 3 == 2){
    read <- as.numeric(unlist(strsplit(line[i],'\t'))[3])
    if (pt != patient){ 
      cat(count)
      cat('\n')
      patient <- pt
      cat(patient)
      cat('\t')
      count <- read
    }
    else{
      count <- count+read
    }
    if (i == long){
      cat(count)
    }
  }
}
sink()    

a1 <- read.table('../logs/readcountfilter.log')
long <- length(a1[,1])
patient <- ''
count <- 0
sink('../logs/filter.dep')
for (i in 1:long){
  pt <- substr(a1[i,1],20,25)
  read <- a1[i,2]
  if (pt != patient){
    cat(count)
    cat('\n')
    patient <- pt
    cat(patient)
    cat('\t')
    count <- read
  }
  else{
    count <- count+read
  }
  if (i == long){
    cat(count)
  }
}
sink()

#minimal coverage and maximal coverage
nucfiles <- list.files(path='../freq/nucfreq/',pattern='.*.freq',full.names=TRUE)
mincov <- 1000000
maxcov <- 0
aa <- 0
for (nucfile in nucfiles){
  a1 <- read.table(nucfile,header=T)
  for (i in 6:1512){
    cov <- sum(a1[i,2:5])
    if (cov < mincov) mincov <- cov 
    if (cov > maxcov) maxcov <- cov
    aa <- c(aa,cov)
  }
}


