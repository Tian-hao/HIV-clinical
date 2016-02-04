#Rcode

ctl <- unlist(read.table('freq/ctl/ctlfitness'))
other <- unlist(read.table('freq/ctl/ctlfitnessno'))
ctl[which(ctl<0.01)] <- 0.01
other[which(other<0.01)] <- 0.01
plot(c(0.5,2.5),c(-2,1),type='n')
points(rep(1,length(ctl)),log(ctl,10))
points(rep(2,length(other)),log(other,10))
p <- t.test(log(ctl,10),log(other,10))$p.value
legend('topright',legend=paste('p=',p,sep=''))
