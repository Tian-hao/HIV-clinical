#!/usr/bin/env python
#count the frequency of fragmental haplotypes in every patient

import os
import sys
import string
from Bio import SeqIO

def getpatient(fasfile):
  patientlist = []
  for handle in SeqIO.parse(fasfile,'fasta'):
    patient = handle.id.rsplit('_')[0]
    if patient not in patientlist:
      patientlist.append(patient)
  return patientlist

def countlethal(fasfile,patient):
  fasfile.seek(0)
  freq = 0
  for handle in SeqIO.parse(fasfile,'fasta'):
    if patient == handle.id.rsplit('_')[0]:
      if len(str(handle.seq)) != 497:
        freq += float(handle.id.rsplit('_')[2])
  return freq

fasfile = open('all.pep','r')
outfile = open('lethal.freq','w')
patientlist = getpatient(fasfile)
for patient in patientlist:
  outfile.write(patient+'\t')
  freq = countlethal(fasfile,patient)
  outfile.write(str(freq)+'\n')
outfile.close()
fasfile.close()
