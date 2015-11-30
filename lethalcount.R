#R code
png('../graph/lethal.png',res=400,width=3600,height=3600)
par(mfrow=c(4,4),cex=0.2)
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
	plot(tmp[,23],type='n',ylim=c(0,1),main=fullname)
	for (i in 1:500){
	  total <- sum(tmp[i,2:23])
 	  if (total > 0 & tmp[i,23]>0) points(tmp[i,1],tmp[i,23]/total)
	  else points(tmp[i,1],1e-4)
	}
      }
    }
  }
}

