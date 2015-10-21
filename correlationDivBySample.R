#R code
#correlation matrix of diversity
#install.packages("vegan")
library(vegan)
panel.cor <- function(x, y, digits = 2, prefix = "", cex.cor, ...)
{
    r <- abs(cor(x, y,method='spearman'))
    usr <- par("usr"); on.exit(par(usr))
    par(usr = c(0, 1, 0, 1))
    rect(0,0,1,1,col=rgb(1-r,0,0,0.5))
    txt <- format(c(r, 0.123456789), digits = digits)[1]
    txt <- paste0(prefix, txt)
    if(missing(cex.cor)) cex.cor <- 0.8/strwidth(txt)
    text(0.5, 0.5, txt, cex = cex.cor * r)
}
png('../graph/correlationMatrixDiversity.png',width=1200,height=1200)
corcount <- list()
for (g in 1:2){
  for (p in 1:5){
    if (p==4) next
    for (t in 1:2){
      fullname <- paste('G',g,'P',p,'T',t,'.*.count',sep='')
      patientfiles <- list.files(path='../freq/freq',pattern=fullname)
      shortname <- paste('G',g,'P',p,sep='')
      pngfile <- paste('../graph/',shortname,'.png',sep='')
      count <- matrix(,nrow=1520,ncol=5)
      count[,1] <- c(1:1520)
      count[,2:5] <- 0
      for (filename in patientfiles){
        tmp <- read.table(paste('../freq/freq/',filename,sep=''),header=F)
        for (i in 2:5){
	  count[,i] <- count[,i]+tmp[,i]
        }
      }
      ddd <- diversity(count[,2:5])
      corcount[[length(corcount)+1]] <- ddd
    }
  }
}  
pairs(corcount,lower.panel = NULL, upper.panel = panel.cor,diag.panel=NULL,text.panel=NULL)
