#!/usr/bin/env python
#sampling some reads for dn/ds calculation

import os
import sys
import string
import random
import bisect
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

def getptlist(recordict):
  ptlist = []
  for seqname in recordict.keys():
    pt = seqname.rsplit('_')[0]+'_'+seqname.rsplit('_')[1]
    if pt not in ptlist:
      ptlist.append(pt)
  return ptlist

def getseqdict(recordict,pt):
  seqlist = []
  freqlist = []
  freq = 0
  seqnames = [seqname for seqname in recordict.keys() if pt in seqname]
  for seqname in seqnames:
    freq += float(seqname.rsplit('_')[2].rstrip())
    seqlist.append(recordict[seqname])
    freqlist.append(freq)
  for i in range(0,len(freqlist)):
    freqlist[i] = freqlist[i]/freq
  return (seqlist,freqlist)

def sampling(seqlist,freqlist,ss):
  sampreads = []
  for readcount in range(0,ss):
    rand = random.random()
    i = bisect.bisect(freqlist,rand)
    sampreads.append(seqlist[i])
  return sampreads

def writefas(samreads,outfile):
  outlist = []
  readcount = 0
  for read in samreads:
    readcount += 1
    record = SeqRecord(Seq(read,IUPAC.extended_dna),id='t'+str(readcount),description="")
    outlist.append(record)
  SeqIO.write(outlist,outfile,'fasta')

def writephylip(sampreads,outfile):
  readcount = len(sampreads)
  readlength = len(sampreads[0])
  outfile.write(' '+str(readcount)+' '+str(readlength)+'\n')
  readcount = 0
  for read in sampreads:
    readcount += 1
    outfile.write('t'+str(readcount)+'\t'+read+'\n')
  outfile.close()

SampleSize = 1000
infile = open('../freq/ctl/epitopeextraction.txt','r')
recordict = {}
for line in infile:
  if 'patient' in line: continue
  line = line.rstrip().rsplit('\t')
  recordict[line[0]+'_'+line[2]+'_'+line[3]] = line[4]
ptlist = getptlist(recordict)
for pt in ptlist:
  outfile = open('../freq/ctl/dnds/'+pt+'.lip','w')
  seqlist, freqlist = getseqdict(recordict,pt)
  print freqlist
  print len(freqlist)
  sampreads = sampling(seqlist,freqlist,SampleSize)
  writefas(sampreads,outfile)
  outfile.close()
infile.close()
  
