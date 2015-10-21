#!/usr/bin/env python
import re
import os
import sys
import glob
import string
from Bio import SeqIO

hlafile = open('../cns/HLA.txt','r')
patientfile = open('../cns/protein.fa','r')
ctlfile = open('../background/escapeMutations.txt','r')
outfileyes = open('../cns/CTLhits.txt','w')
outfileno = open('../cns/CTLnohits.txt','w')
hlahash = {}
ctlhash = {}
for line in ctlfile.xreadlines():
  line = re.split(r'\t+',line.rstrip('\t'))
  ctllist = [] #ctllist[0] is pos, ctllist[1] is mut
  ctllist.append(line[2])
  ctllist.append(line[3].rstrip('\n'))
  ctlhash[line[1]] = ctllist
for line in hlafile.xreadlines():       #Error: one HLA has multiple escape
  line = re.split(r'\t+',line.rstrip('\t'))
  hlalist = []
  for i in range(1,5):
    hlalist.append(line[i])
  hlahash[str(line[0])] = hlalist
for record in SeqIO.parse(patientfile,'fasta'):
  for seqname in hlahash.keys():
    if seqname==str(record.id):
      HLAnames = hlahash[str(record.id)]
      for hlaname in HLAnames:
        if hlaname in ctlhash.keys():
          pos = int(ctlhash[hlaname][0])
          mut = ctlhash[hlaname][1]
          if str(record.seq)[pos-1]==mut:
            outfileyes.write(str(record.id)+'\t'+str(pos)+'\t'+mut+'\t'+hlaname+'\n')
          else:
            outfileno.write(str(record.id)+'\t'+str(pos)+'\t'+mut+'\t'+hlaname+'\n')

