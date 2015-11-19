#!/usr/bin/env python
import os
import sys
import string
from Bio import SeqIO
from math import log

infile = open('all.fas','r')
seqlist = []
ptlist = []
for handle in SeqIO.parse(infile,'fasta'):
  seqlist.append(str(handle.id))
  name = str(handle.id).rsplit('_')[0]
  if name not in ptlist:
    ptlist.append(name)
for ptname in ptlist:
  sdi = 0
  seqcount = 0
  for seq in seqlist:
    if ptname in seq:
      freq = float(seq.rsplit('_')[2])
      sdi -= freq*log(freq)
      seqcount += 1
  if seqcount == 1:
    print ptname+'\t'+str(sdi)
  else:
    print ptname+'\t'+str(sdi/log(seqcount))
