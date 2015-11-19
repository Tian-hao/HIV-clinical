#!/usr/bin/env python
import os
import sys
import glob
import string
from Bio import SeqIO

infile = open('raw/G1P1T1global_27_1515.fas','r')
outfile = open('raw/G1P1T1global_27_1515new.fas','w')
seqcount = 0
outlist = []
for handle in SeqIO.parse(infile,'fasta'):
  seqcount += 1
  handle.id = str(seqcount)
  handle.description = ''
  outlist.append(handle)
SeqIO.write(outlist,outfile,'fasta')
