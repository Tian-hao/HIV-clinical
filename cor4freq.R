#R code
library("RColorBrewer")
freqfiles <- list.files(path='.',pattern='G.*.freq')
pdf('cor4freq.pdf',width=20,height=20)
par(mfrow=c(4,4))
mycol <- brewer.pal(4,"Set2")
for (freqfile in freqfiles){
  patient <- strsplit(freqfile,'_cor.freq')[1]
  freq <- read.table(freqfile,header=T)
  plot(freq[,2],freq[,6],col=mycol[1],pch=4,xlab='haplotype',ylab='rawdata',main=patient)
  points(freq[,3],freq[,7],col=mycol[2],pch=4)
  points(freq[,4],freq[,8],col=mycol[3],pch=4)
  points(freq[,5],freq[,9],col=mycol[4],pch=4)
  legend('topleft',c('A','T','C','G'),pch=4,col=mycol)
}
