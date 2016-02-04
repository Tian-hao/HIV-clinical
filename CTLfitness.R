#Rcode
#Does virus in  elite controller carry more deleterious mutations at CTL region?
a1 <- read.table('../freq/ctl/epitopefitness.txt',header=T)
g1fit <- 1
g2fit <- 1
fitlist <- as.numeric(levels(a1[,7]))
for (i in 1:length(a1[,1])){
  group = substr(a1[i,1],2,2)
  fitness = fitlist[a1[i,7]]
  freq = a1[i,6]
  if (!is.na(fitness) && group == '1') { g1fit <- g1fit*(fitness)^freq; g1tmp <- g1tmp*(fitness)^freq}
  if (!is.na(fitness) && group == '2') { g2fit <- g2fit*(fitness)^freq; g2tmp <- g2tmp*(fitness)^freq}
}
print(g1fit)
print(g2fit)
