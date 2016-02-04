#!/usr/bin/env python
import os
import sys
import glob
import pysam
import string
from Levenshtein import *

def ifnsmt(codon):
  if hamming(codon,'TGA')==1: return 1
  if hamming(codon,'TAG')==1: return 1
  if hamming(codon,'TAA')==1: return 1
  else: return 0

def readcns(cnsfile):
  refseq = ''
  for line in cnsfile:
    if '>' in line: continue
    refseq += line.rstrip()
  return refseq[26::]

def getlist(refseq):
  reflist = []
  i = 0
  nsmt = 0
  tgg = 0
  while i < len(refseq)-3:
    reflist.append(refseq[i:i+3])
    if ifnsmt(refseq[i:i+3]): nsmt += 1
    if refseq[i:i+3]=='TGG': 
      tgg += 1
      print i/3
    i += 3
  print nsmt
  print tgg
  return reflist

def readbam(bamfile,reflist,qs):
  aafreq = {}
  stoplist = ['TGA','TAG','TAA','XXX','TGG']
  for i in range(0,len(reflist)):
    aafreq[i] = {}
    for codon in stoplist:
      aafreq[i][codon] = 0
  for line in bamfile:
    if min(line.query_qualities) < qs: continue
    if line.reference_start < 24: continue
    transtart_que = 2 - line.reference_start % 3
    transtart_pep = (line.reference_start - 24)/3
    pepseq = line.query_sequence[transtart_que::]
    if len(pepseq)/3+transtart_pep > len(reflist): continue
    i = 0
    while i < len(pepseq)-3:
      if  pepseq[i:i+3] == 'TGA': aafreq[i/3+transtart_pep]['TGA'] += 1
      elif  pepseq[i:i+3] == 'TAG': aafreq[i/3+transtart_pep]['TAG'] += 1
      elif  pepseq[i:i+3] == 'TAA': aafreq[i/3+transtart_pep]['TAA'] += 1
      else: aafreq[i/3+transtart_pep]['XXX'] += 1
      if  reflist[i/3+transtart_pep] == 'TGG': aafreq[i/3+transtart_pep]['TGG'] += 1
      i += 3
  return aafreq

def writefreq(outfile,aafreq):
  stoplist = ['TGA','TAG','TAA','TGG']
  outfile.write('pos')
  for aa in stoplist:
    outfile.write('\t'+aa)
  outfile.write('\n')
  for i in range(0,len(aafreq.keys())):
    outfile.write(str(i))
    total = aafreq[i]['TGA']+aafreq[i]['TAG']+aafreq[i]['TAA']+aafreq[i]['XXX']
    total = float(total)
    for aa in stoplist:
      outfile.write('\t'+str(aafreq[i][aa]/total))
    outfile.write('\n')

qs = 20
cnsfile = open('../freq/pilot/G1P2T2.cns')
refseqs = readcns(cnsfile)
reflist = getlist(refseq)
cnsfile.close()
bamfile = pysam.AlignmentFile('../bams/G1P2T2_aa.bam','rb')
aafreq = readbam(bamfile,reflist,qs)
bamfile.close()
outfile = open('../freq/pilot/stopfreq.txt','w')
writefreq(outfile,aafreq)
outfile.close()

