#!/usr/bin/env python
import os
import sys
import string
from Bio import SeqIO

infile = open('raw/G1P1T1global_27_1515.fas','r') #this is your input file
outfile = open('allsort.pep','w') 
seqdict = {}
for handle in SeqIO.parse(infile,'fasta'):
  freq = handle.description.rsplit('Freq:')[1].rsplit('. Overlap')[0]
  freq = float(freq)
  seqdict[freq] = handle
  freqlist = sorted(seqdict.keys(),reverse=True)
outlist = []
for freq in freqlist:
  outlist.append(seqdict[freq])
SeqIO.write(outlist,outfile,'fasta')
infile.close()
outfile.close()
