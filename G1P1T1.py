#!/usr/bin/env python
import os
import sys
import glob
import string
from Bio import SeqIO

tar = sys.argv[1]
combinedfile = open('all.fas','r')
outfile = open('G1P1T1.fas','w')
outlist = []
for handle in SeqIO.parse(combinedfile,'fasta'):
  line = str(handle.id).rsplit('_')
  if tar in line[0]:
    handle.id = line[0]+'_'+line[1]
    handle.description=''
    outlist.append(handle)
SeqIO.write(outlist,outfile,'fasta')
  
