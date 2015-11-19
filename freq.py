#!/usr/bin/env python
import os
import sys
import glob
import string
from Bio import SeqIO

infile = open('all.fas','r')
outfile = open('G1P1.freq','w')
freqlist = []
seqdict = {}
for handle in SeqIO.parse(infile,'fasta'):
  line = str(handle.id).rsplit('_')
  if 'G1P1T2' in line[0]:
    name = line[0]+'_'+line[1]
    freq = float(line[2].rstrip())
    freqlist.append(freq)
    seqdict[freq] = name
freqlist = sorted(freqlist,reverse=True)
for freq in freqlist:
  outfile.write(seqdict[freq]+'\t'+str(freq)+'\n')

