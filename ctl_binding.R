#Rcode

f1 <- read.table('freq/ctl/bindingcor')
plot(log(f1[,2],10),log(f1[,3],10))
cor.test(f1[,2],f1[,3],method='spearman')
