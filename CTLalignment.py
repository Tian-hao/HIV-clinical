#!/usr/bin/env python
import os
import sys
from Bio import pairwise2
from Bio import SeqIO

cnsfile = open('../cns/protein.fa','r')
ctlfile = open('../background/CTL.txt','r')
outfile = open('../cns/algns.txt','w')
sumfile = open('../cns/algnSummary.txt','w')
cnslist = {}
ctllist = []
for record in SeqIO.parse(cnsfile,'fasta'):
  cnslist[str(record.id)] = str(record.seq)
for line in ctlfile.xreadlines():
  line = line.rstrip()
  ctllist.append(line)
for ctl in ctllist:
  for cns in cnslist.keys():
    algns = pairwise2.align.localms(ctl,cnslist[cns],1,-1,-100,-10)
    outfile.write(algns[0][0]+'\n'+algns[0][1]+'\n\n')
    if (algns[0][2]==len(ctl)): sumfile.write(ctl+'\t'+cns+'\n')
