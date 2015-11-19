#!/usr/bin/env python
#split file for cytoscape
import os
import sys
import math

infile = open('ctl.freq','r')
ptfile = open('patientctl.txt','r')
for line in ptfile:
  pt = line.rsplit('\t')[0]
  outfile = open(pt+'ctl.freq','w')
  outfile.write('haplotype\tfreq\tphenotype\n')
  infile.seek(0)
  for haplo in infile:
    haplo = haplo.rstrip().rsplit('\t')
    if haplo[0].rsplit('T')[0] == pt:
      outfile.write(haplo[0]+'\t'+str(math.sqrt(float(haplo[1])))+'\t#'+haplo[2]+'\n')
  outfile.close()
infile.close()
ptfile.close()
      

