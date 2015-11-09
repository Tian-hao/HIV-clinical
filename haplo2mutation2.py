#!/usr/bin/env python
#implement PredictHaplo, count nucleotide frequencies

import os
import sys
import glob
from Bio import SeqIO

def getpatient(fasfile):
  patientlist = []
  for handle in SeqIO.parse(fasfile,'fasta'):
    patient = handle.id.rsplit('_')[0]
    if patient not in patientlist:
      patientlist.append(patient)
  return patientlist

def countfreq(fasfile,patient):
  seqdict = {}
  freqdict = {}
  fasfile.seek(0)
  for handle in SeqIO.parse(fasfile,'fasta'):
    line = handle.id.rsplit('_')
    if patient == line[0]:
      seq = handle.seq
      freq = line[2]
      seqdict[seq] = float(freq)
  for i in range(0,1489):
    basedict = {}
    for seq in seqdict.keys():
      if seq[i] in basedict.keys():
        basedict[seq[i]] += seqdict[seq]
      else:
        basedict[seq[i]] = seqdict[seq]
    for base in basedict.keys():
      freqdict[str(i)+base] = basedict[base]
  return freqdict

baselist = ['A','T','C','G']
fasfile = open('all.fas','r')
patientlist = getpatient(fasfile)
for patient in patientlist:
  outfile = open(patient+'.freq','w')
  freq = countfreq(fasfile,patient)
  outfile.write('pos\tA\tT\tC\tG\n')
  for i in range(0,1489):
    outfile.write(str(i+1)+'\t')
    for base in baselist:
      if str(i)+base in freq.keys():
        outfile.write(str(freq[str(i)+base])+'\t')
      else:
        outfile.write('0\t')
    outfile.write('\n')
  outfile.close()
fasfile.close()
