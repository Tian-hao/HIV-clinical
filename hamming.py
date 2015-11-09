#!/usr/bin/env python
import os 
import sys
import string
from Levenshtein import *
from Bio import SeqIO

nucfile = open('all.fasta','r')
nucdis = open('nuc.ham','w')
record = {}
for read in SeqIO.parse(nucfile,'fasta'):
  record[str(read.id)] = str(read.seq)
for seqA in record.keys():
  for seqB in record.keys():
    nucdis.write(seqA+'\t'+seqB+'\t'+str(hamming(record[seqA],record[seqB]))+'\n')
  
