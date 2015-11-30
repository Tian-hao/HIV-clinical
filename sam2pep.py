#!/usr/bin/env python
import os
import sys
import glob
import pysam
import string
from Bio import SeqIO

def translation(seq):
  dnamap = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"_", "TAG":"_",
    "TGT":"C", "TGC":"C", "TGA":"_", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G", "XXX":"X"}
  pep = []
  i = 0
  seq = str(seq).translate(None,"-")
  while i < len(seq):
    codon = seq[i:i+3]
    if codon not in dnamap.keys():
      aa = 'X'
    elif len(codon) != 3:
      aa = ''
    else:
      aa = dnamap[codon]
    pep.append(aa)
    i = i + 3
  pep = ''.join(pep)
  return pep

def readbam(bamfile,qs):
  aafreq = {}
  for i in range(0,530):
    aafreq[i] = {}
  for line in bamfile:
    if min(line.query_qualities) < qs:
      continue
    if line.reference_start < 24:
      continue
    transtart_que = 2 - line.reference_start % 3
    transtart_pep = (line.reference_start - 24)/3
    pepseq = translation(line.query_sequence[transtart_que:-1])
    for pos in range(0,len(pepseq)):
      if pepseq[pos] in aafreq[pos+transtart_pep].keys():
        aafreq[pos+transtart_pep][pepseq[pos]] += 1
      else:
        aafreq[pos+transtart_pep][pepseq[pos]] = 1
  return aafreq

def writefreq(outfile,aafreq):
  AA = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q',
    'L','M','N','V','W','Y','X','_']
  freqfile = open(outfile,'w')
  freqfile.write('pos')
  for aa in AA:
    freqfile.write('\t'+aa)
  freqfile.write('\n')
  for i in range(0,500):
    freqfile.write(str(i))
    for aa in AA:
      if aa in aafreq[i].keys():
        freqfile.write('\t'+str(aafreq[i][aa]))
      else:
        freqfile.write('\t0')
    freqfile.write('\n')

QualityScore = 20
path2sam = '../bams/'
path2out = '../bams/'
samfiles = sorted(glob.glob(path2sam+'G*aa.sam'))
reffile = open('../ref/ref.fa','r')
for samfile in samfiles:
  sortbam = samfile.rsplit('.sam')[0]+'s.bam'
  os.system('samtools view -hbSF4 '+samfile+' | samtools sort -T ../tmp/aln.tmp > '+sortbam)
  os.system('samtools index '+sortbam)
  bamfile = pysam.AlignmentFile(sortbam,'rb')
  aafreq = readbam(bamfile,QualityScore)
  outfile = path2out+samfile.rsplit(path2sam)[1].rsplit('.sam')[0]+'.freq'
  writefreq(outfile,aafreq)
