#R code
#false positive rate of outside BC.

error = 0.001
length = 100
depth = 1000000
cutoff = 20
BC = 600

errorreads = dbinom(1,length,error)*depth
errordepth = round(errorreads/length)
clustersampling = dbinom(cutoff,errordepth,1/BC)
fspos = 1-(1-clustersampling)^length

