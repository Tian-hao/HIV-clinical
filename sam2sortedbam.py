#!/usr/bin/env python

import os
import sys
import glob
import string

path2sam = '../errorcorrection/'
path2bam = '../errorcorrection/'
path2tmp = '../errorcorrection/'
samfiles = sorted(glob.glob(path2sam+'*.sam'))
for samfile in samfiles:
  samname = samfile.rsplit(path2sam)[1].rsplit('.sam')[0]
  os.system('samtools view -bS '+samfile+' > '+path2bam+samname+'.bam')
  os.system('samtools sort -T '+path2tmp+samname+'.tmp'+' -O bam '+path2bam+samname+'.bam > '+path2bam+samname+'.sorted.bam')
