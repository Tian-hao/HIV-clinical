#!/usr/bin/env python
import os
import sys
import glob
import string 
from Bio import SeqIO

filenames = sorted(glob.glob('G*.fas'))
combinedfile = open('all.fas','w')
outlist = []
for filename in filenames:
  fasfile = open(filename,'r')
  for haplo in SeqIO.parse(fasfile,'fasta'):
    freq = haplo.description.rsplit('Freq:')[1].rsplit('. Overlap')[0]
    haplo.id = filename.rsplit('global')[0]+'_S'+str(haplo.id).rsplit('_')[1].rsplit('.')[0]+'_'+freq
    haplo.name = haplo.id
    haplo.description = haplo.id
    outlist.append(haplo)
SeqIO.write(outlist,combinedfile,'fasta')
