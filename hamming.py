#!/usr/bin/env python
import os 
import sys
import string
from Levenshtein import *
from Bio import SeqIO

filename = sys.argv[1]
nucfile = open(filename,'r')
nucdis = open('nuc.ham','w')
record = {}
for read in SeqIO.parse(nucfile,'fasta'):
  record[str(read.id)] = str(read.seq)
for seqA in sorted(record.keys()):
  for seqB in sorted(record.keys()):
    nucdis.write(seqA+'\t'+seqB+'\t'+str(distance(record[seqA],record[seqB]))+'\n')
  
