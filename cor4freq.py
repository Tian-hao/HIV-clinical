#!/usr/bin/env python
#correlation of mutation frequency in haplotype data and original dataset
import os
import sys
import glob
import string

filenames = sorted(glob.glob('freq/*.freq'))
for filename in filenames:
  rawname = '../../freq/freq/'+filename.rsplit('freq/')[1].rsplit('.freq')[0]+'_aa.freq'
  outname = filename.rsplit('freq/')[1].rsplit('.freq')[0]+'_cor.freq'
  haplofile = open(filename,'r')
  rawfile = open(rawname,'r')
  outfile = open(outname,'w')
  line2 = rawfile.readlines()
  for line1 in haplofile.xreadlines():
    line1 = line1.rsplit('\t')
    if line1[0] == 'pos': 
      outfile.write('pos\tA\tT\tC\tG\tA\tT\tC\tG\n')
      continue
    line = line2[25+int(line1[0])].rstrip().rsplit('\t')
    outfile.write(line1[0]+'\t'+line1[1]+'\t'+line1[2]+'\t'+line1[3]+'\t'+line1[4]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]+'\t'+line[4]+'\n')
  outfile.close()
  rawfile.close()
  haplofile.close()
