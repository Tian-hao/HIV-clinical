#!/usr/bin/env python
#count haplotype distribution
import os
import sys
import glob
import string
from Bio import SeqIO

haplofiles = sorted(glob.glob('../quasiRecomb/test1/*.fasta'))
for haplofile in haplofiles:
  outfile = haplofile.rsplit('.fasta')[0]+'.txt'
  haplohandle = open(haplofile,'r')
  outhandle = open(outfile,'w')
  haploseq = {}
  for record in SeqIO.parse(haplohandle,'fasta'):
    freq = float(record.id.rsplit('_')[1])
    if record.seq in haploseq.values():
      haploseq[record.seq] += freq
    else:
      haploseq[record.seq] = freq
  for seq in haploseq.keys():
    outhandle.write(str(seq)+'\t'+str(haploseq[seq])+'\n')
  haplohandle.close()
  outhandle.close()
