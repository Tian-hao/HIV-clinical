#R code
library("RColorBrewer")
library("gplots")
hmcol<-brewer.pal(11,"RdYlBu")
heatable <- read.table('pepheat.tab',header=T)
heat <- as.matrix(heatable)
class(heat) <- 'numeric'
rownames(heat) <- c(colnames(heat)[2:97])
heat[heat[,]>100] <- 100
pdf('pepheat.pdf',height=12,width=12)
heatmap.2(heat[1:96,2:97],Rowv=NA,Colv=NA,scale='none',col=hmcol,trace='none',density.info='none')
