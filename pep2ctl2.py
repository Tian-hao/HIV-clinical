#!/usr/bin/env python
#[12, 26, 28, 30, 31, 76, 79, 83, 86, 93, 109, 119, 127, 146, 147, 182, 186, 211, 242, 268, 280, 286, 302, 303, 312, 326, 331, 339, 340, 357, 374, 397, 398, 401, 403, 437, 441, 482]
import os
import sys
import re
import string
from Bio import SeqIO

def readctl(ctlfilename):
  escapedict = {}
  ctlfile = open(ctlfilename,'r')
  for line in ctlfile.xreadlines():
    line = line.rstrip().rsplit('\t')
    if line[1] in escapedict.keys():
      escapedict[line[1]] += (line[2]+line[3])
    else:
      escapedict[line[1]] = (line[2]+line[3])
  ctlfile.close()
  return escapedict

def readpatient(ptfilename):
  patientdict = {}
  ptfile = open(ptfilename,'r')
  for line in ptfile.xreadlines():
    line = line.rstrip().rsplit('\t')
    patientdict[line[0]] = line[1]
  return patientdict

def getpos(hlatype,escapedict):
  poslist = []
  hlalist = hlatype.rsplit('/')
  for hla in hlalist:
    if hla not in escapedict.keys(): continue
    hlatarget = escapedict[hla]
    hlatarget = re.findall('\d+', hlatarget)
    for pos in hlatarget:
      if int(pos) not in poslist:
        poslist.append(int(pos))
  poslist.sort()
  return poslist

def readmut(mutfilename):
  escapemut = {}
  mutfile = open(mutfilename,'r')
  for line in mutfile.xreadlines():
    line = line.rstrip().rsplit('\t')
    if line[2] in escapemut.keys():
      escapemut[line[2]] += line[3]
    else:
      escapemut[line[2]] = line[3]
  mutfile.close()
  return escapemut

def readhaplo(pepfilename,escapedict,patientdict,escapemut):
  haplodict = {}
  pepfile = open(pepfilename,'r')
  for record in SeqIO.parse(pepfile,'fasta'):
    haplodict[str(record.id)] = ''
    patient = str(record.id).rsplit('T')[0]
    poslist = getpos(patientdict[patient],escapedict)
    escapenum = 0
    for pos in poslist:
      if pos > len(str(record.seq)): 
        haplodict[str(record.id)] += '0'
      elif str(record.seq)[pos-1] in escapemut[str(pos)]:
        haplodict[str(record.id)] += '1'
	freq = float(str(record.id).rsplit('_')[2])
	escapenum += freq
      else:
        haplodict[str(record.id)] += '0'
    #if len(str(record.seq)) < 496:
        #haplodict[str(record.id)] += 'x'
    haplodict[str(record.id)] = [escapenum,len(poslist)]
  return haplodict

escapedict = readctl('escapeMutations.txt')
escapemut = readmut('escapeMutations.txt')
patientdict = readpatient('patientctl.txt')
haplodict = readhaplo('all.pep',escapedict,patientdict,escapemut)
outfile = open('ctl.freq','w')
for haplo in sorted(haplodict.keys()):
  line = haplo.rsplit('_')
  name = line[0]+'_'+line[1]
  freq = line[2]
  phenotype = haplodict[haplo][0]
  posnum = haplodict[haplo][1]
  outfile.write(name+'\t'+freq+'\t'+str(phenotype)+'\t'+str(posnum)+'\n')
outfile.close()
