#!/usr/bin/env python
import os
import sys
import string
import random
import bisect

def getsample(ctlfile):
  splist = []
  ctlhandle = open(ctlfile,'r')
  for line in ctlhandle:
    line = line.rstrip().rsplit('\t')
    line2 = line[2].rsplit('_')
    line = line[0]+'_'+line[1]+'_'+line2[0]+'_'+line2[1]
    splist.append(line)
  ctlhandle.close()
  return splist

def getfreq(sample,p2freq,time):
  freqdict = {}
  freqfile = p2freq+sample.rsplit('_')[0]+time+'.freq'
  freqhandle = open(freqfile,'r')
  aalist = freqhandle.readline()
  ctlpos = int(sample.rsplit('_')[3])
  ctllen = len(sample.rsplit('_')[2])
  for i,line in enumerate(freqhandle):
    if i+1 < ctlpos or i+1 >= ctlpos+ctllen: continue
    line = line.rstrip().rsplit('\t')[1::]
    countlist = []
    cumfreq = 0
    for aafreq in line:
      cumfreq += float(aafreq)
      countlist.append(cumfreq)
    freqlist = []
    for count in countlist:
      freqlist.append(count/cumfreq)
    freqdict[i-ctlpos+1] = freqlist
  freqhandle.close()
  return freqdict

def getaalist(infile):
  inhandle = open(infile)
  aalist = inhandle.readline().rstrip().rsplit('\t')[1::]
  inhandle.close()
  return aalist

def randseq(aalist,freqdict):
  seq = ''
  for pos in freqdict.keys():
    freqlist = freqdict[pos]
    rand = random.random()
    i = bisect.bisect(freqlist,rand)
    seq += aalist[i]
  return seq

def writesample(aalist,freqdict,outfile):
  outhandle = open(outfile,'w')
  for i in range(0,1000):
    outhandle.write('>'+str(i+1)+'\n')
    seq = randseq(aalist,freqdict)
    outhandle.write(seq+'\n')
  outhandle.close()
   
samplelist = getsample('../freq/ctl/ctl.txt')
path2freq = '../freq/pepfreq/'
aalist = getaalist('../freq/pepfreq/G1P1T1.freq')
for sample in samplelist:
  freqdict1 = getfreq(sample,path2freq,'T1')
  freqdict2 = getfreq(sample,path2freq,'T2')
  writesample(aalist,freqdict1,'../freq/ctl/sampling/'+sample+'_T1.fa')
  writesample(aalist,freqdict2,'../freq/ctl/sampling/'+sample+'_T2.fa')
