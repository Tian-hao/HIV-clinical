#R code
#1 library. 200bp. sequence in two fragments. 
#mutation rate, 1 per genome.

seed <- as.double(0.03)
RANDU <- function() {
  seed <<- ((2^16 + 3) * seed) %% (2^31)
  seed/(2^31)
}

MutGen <- function(MutRate) {
  Gen <- 14
  length <- 200
  seq <- matrix(nrow=Gen,ncol=length*2^Gen)
  for(k in 1:length) {
    seq[1,k] <- 0
  }
  flag <- 1
  for(i in 2:Gen) {
    for(j in 1:2^(i-1)) {
      for(k in 1:length) {
        if (flag==1) {
          seq[i,k+(j-1)*length] <- seq[i-1,k+floor((j-1)/2)*length]
        }
        else if ((RANDU() < MutRate) && (flag==0)) {
          seq[i,k+(j-1)*length] <- 1
        }
        else seq[i,k+(j-1)*length] <- seq[i-1,k+floor((j-1)/2)*length]
      }
      if (flag==1) { flag <- 0 }
      else if (flag==0) { flag <- 1 }
    }
  }
  error <- vector()
  for(k in 1:length) {
    error[k] <- 0
  }  
  for(j in 1:2^(Gen-1)) {
    for(k in 1:length) {
      error[k] <- error[k] + seq[Gen,k+(j-1)*length]
    }
  }
  error <- error/2^(Gen-1)
  return(error)
}

RealWT <- function(reads,mutDist) {
  realwt <- reads
  for (i in 1:200) {
    realwt <- realwt*(1-mutDist[i])
  }
  return(realwt)
}

SingleMut <- function(reads,mutDist) {
  singlemut <- vector()
  for(i in 1:200) {
    singlemut[i] <- reads
    for (j in 1:200) {
      if (j==i) { singlemut[i] <- singlemut[i] * mutDist[j]}
      else {
        singlemut[i] <- singlemut[i]*(1-mutDist[j])
      }
    }
  }
  return(singlemut)
}

#normal distribution
#Fitness <- function() {    
#  fitness <- rnorm(n=200,m=0,sd=5)
#  fitness <- 2^fitness
#  return(fitness)
#}

#one beneficial
#Fitness <- function() {
#  fitness <- vector()
#  for (i in 1:200) {
#    fitness[i] <- 0.8
#  }
#  fitness[50] <- 5
#  return(fitness)
#}

#expo distribution
Fitness <- function() {
  fitness <- rexp(n=200,rate=2)
  fitness[50] <- 500
  return(fitness)
}

Selection <- function(singlemut,reads,fitness) {
  singlemut <- singlemut / reads
  for (i in 1:200) {
    singlemut[i] <- singlemut[i]*fitness[i]
  }
  return(singlemut)
}

CallFitness <- function(singlemut,singlemut2,reads,realwt){
  singlemut2 <- singlemut2/(sum(singlemut2)+realwt)*reads
  newfitness <- vector()
  prewt1 <- sum(singlemut[101:200])+realwt
  prewt2 <- sum(singlemut[1:100])+realwt
  postwt1 <- sum(singlemut2[101:200])+realwt
  postwt2 <- sum(singlemut2[1:100])+realwt
  print(prewt1)
  print(prewt2)
  print(postwt1)
  print(postwt2)
  for (i in 1:100) {
    newfitness[i] <- singlemut2[i]/singlemut[i]
  }
  for (i in 101:200) {
    newfitness[i] <- singlemut2[i]/singlemut[i]
  }
  return(newfitness)
}

  reads <- 1000000
  mutationrate <- 10^-3
  mutDist <- MutGen(mutationrate)
  png('../background/simuD.png')
  plot(mutDist)
  realwt <- RealWT(reads,mutDist)
  print(realwt/reads)
  singlemut <- SingleMut(reads,mutDist)
  png('../background/simu.png')
  plot(singlemut)
  fitness <- Fitness()
  singlemut2 <- Selection(singlemut,reads,fitness)*reads
  png('../background/simu2.png')
  plot(singlemut2)
  newfitness <- CallFitness(singlemut,singlemut2,reads,realwt)
  png('../background/simuF.png')
  plot(newfitness,log='y',ylim=c(10e-3,5))
  points(fitness,col=2)

  



