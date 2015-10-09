#!/usr/bin/env python

import os
import sys
import glob
import string
from Bio import SeqIO

fqfiles = glob.glob('../bcs/G2P5*')
for fqfile in fqfiles:
  filename = fqfile.rsplit('/bcs/')[1].rsplit('_R1_')[0]
  os.system('mkdir ../bcs/'+filename)
  os.system('mv '+fqfile+' ../bcs/'+filename)
  fqfile2 = fqfile.replace('_R1_','_R2_')
  os.system('mv '+fqfile2+' ../bcs/'+filename)
  os.system('../NGSTagErrCorrect/script/Fastq2ErrorFreeFasta.py -i ../bcs/'+filename+' -o ../errorcorrection/'+filename+' -F _R1_ -R _R2_ -d 2 -b 1-3 -p 4-12 -e 0.9 -s 2')

