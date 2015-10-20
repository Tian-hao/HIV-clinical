#!/usr/bin/env python
import os
import sys
import string
from Bio import SeqIO

ctlfile = open('../background/escapeCTL.txt','r')
cnsfile = open('../cns/protein.fa','r')
outfile = open('../cns/escapehit.txt','w')
cnslist = {}
ctllist = {}
for line in ctlfile.xreadlines():
  line = line.rstrip()
  pos = [int(s) for s in line.split() if s.isdigit()]
  mut = line[-1]
  ctllist[pos[0]] = mut
for record in SeqIO.parse(cnsfile,'fasta'):
  cnslist[str(record.id)] = str(record.seq)
  for pos in ctllist.keys():
    if str(record.seq)[pos-1]==ctllist[pos]:
      outfile.write(str(record.id)+'\t'+str(pos)+'\t'+ctllist[pos]+'\n')
