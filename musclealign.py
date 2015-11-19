#!/usr/bin/env python
import os
import sys
import glob

files = sorted(glob.glob('G*.lip'))
for infile in files:
  outfile = infile.rsplit('.lip')[0]+'.aln'
  os.system('muscle -in '+infile+' -out '+outfile+' -phyi')
