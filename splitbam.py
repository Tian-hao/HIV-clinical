#!/usr/bin/env python
#split sorted bam files to small files
#need index file (.bai) in the same folder

import os
import sys
import glob
import string
import pysam

path2infile = '/Volumes/Yushen/sorted/'
path2outfile = '/Volumes/Yushen/sorted/split/'
path2tmp = '../tmp/'
NUM = 5
infiles = sorted(glob.glob(path2infile+'*1P1T1_aasorted.bam'))
for infile in infiles:
  print 'working on '+infile
  os.system('samtools index '+infile)
  inbam = pysam.AlignmentFile(infile,'rb')
  header = inbam.header
  outfile = {}
  outbam = {}
  newname = {}
  for i in range(1,NUM+1):
    newname[i] = infile.rsplit(path2infile)[1].rsplit('sorted.bam')[0]+'ss'+str(i)+'sorted.sam'
    outfile[i] = path2tmp+newname[i]
    outbam[i] = pysam.AlignmentFile(outfile[i],'wh',header=header)
  handle = inbam.fetch("Gag_pol")
  readcount = 0
  for read in handle:
    readcount += 1
    if (readcount % NUM == 0):
      outbam[NUM].write(read)
    else:
      outbam[readcount % NUM].write(read)
  inbam.close()
  for i in range(1,NUM+1):
    outbam[i].close()
    os.system('samtools view -bSF4 '+path2tmp+newname[i]+' | samtools sort -T '+path2tmp+' -O bam > '+path2outfile+newname[i]+'.bam')
    os.system('rm '+path2tmp+newname[i])
    os.system('samtools index '+path2outfile+newname[i]+'.bam')
    

