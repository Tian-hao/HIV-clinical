#R code
library("RColorBrewer")
library("gplots")
hmcol<-brewer.pal(11,"RdYlBu")
heatable <- read.table('nucheat.tab',header=T)
heat <- as.matrix(heatable)
class(heat) <- 'numeric'
rownames(heat) <- c(colnames(heat)[2:29])
heat[heat[,]>100] <- 100
png('nucheat.png',res=200,height=1000,width=1000)
heatmap.2(heat[1:28,2:29],Rowv=NA,Colv=NA,scale='none',col=hmcol,trace='none',density.info='none')
