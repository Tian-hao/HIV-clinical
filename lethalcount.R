#R code
png('../graph/lethal.png',res=200,width=1800,height=1200)
par(mfrow=c(4,4))
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.freq',sep='')
      patientfiles <- list.files(path='../bams',pattern=fullname)
      shortname <- paste('G',g,'P',p,sep='')
      pngfile <- paste('../graph/',shortname,'.png',sep='')
      #if (t==1){
      #  png(pngfile)
      #}
      for (filename in patientfiles){
        tmp <- read.table(paste('../bams/',filename,sep=''),header=T)
	plot(tmp[,23],main=fullname)
      }
    }
  }
}

