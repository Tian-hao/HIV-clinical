#!/usr/bin/env python

import os
import sys
import string
import glob
from Bio import SeqIO
import pysam

samnames = sorted(glob.glob('../bams/G1P1T1_R1.sorted.bam'))
for R1file in samnames:
  R2file = R1file.replace('_R1','_R2')
  R1sam = pysam.AlignmentFile(R1file,'rb')
  #R2sam = pysam.AlignmentFile(R2file,'rb') 
  count1f = 0
  count1r = 0
  #count2f = 0
  #count2r = 0
  for read in R1sam.fetch(): 
    if read.flag == 0:
      count1f += 1
    if read.flag == 16:
      count1r += 1
  #for read in R2sam.fetch():
    #if read.flag == 0:
      #count2f += 1
    #if read.flag == 16:
      #count2r += 1
  R1sam.close()
  #R2sam.close()
  print count1f, count1r
  #print count2f, count2r

