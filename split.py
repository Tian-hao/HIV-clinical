#! /usr/bin/python
import os
import sys
import glob
import string
import operator
from Bio import SeqIO

def splitfile(R1file,R2file,R1outfiles,R2outfiles,taghash):
  countread = 0
  R2handle = SeqIO.parse(R2file,"fastq")
  for record_R1 in SeqIO.parse(R1file,"fastq"):
    countread += 1
    if countread%10000 == 0: print 'finish processing %d reads' % countread
    record_R2 = R2handle.next()
    ID_R1  = record_R1.id
    ID_R2  = record_R2.id
    assert(ID_R1 == ID_R2)
    seq_R1 = str(record_R1.seq)
    seq_R2 = str(record_R2.seq)
    MID_R1 = seq_R1[0:3]
    MID_R2 = seq_R2[0:3]
    if MID_R1 == MID_R2 and MID_R1 in taghash.keys():
      R1outfiles[MID_R1].write(record_R1.format('fastq'))
      R2outfiles[MID_R2].write(record_R2.format('fastq'))

tagfile = open("../tag",'r')
filenames = sorted(glob.glob('../data/*R1*.fastq'))
taghash = {}
errorbc = []
for line in tagfile.xreadlines():
  line = line.rstrip().rsplit("\t")
  taghash[line[0]] = int(filter(str.isdigit,line[1]+line[2]+line[3]))
  if int(line[4]) == 1: errorbc.append(line[4])
R1outfiles = {}
R2outfiles = {}
for tag in taghash.keys():
  group   = taghash[tag]//100
  patient = (taghash[tag]//10)%10
  time    = taghash[tag]%10
  if tag in errorbc:
    R1outfiles[tag] = open('../split/G'+str(group)+'P'+str(patient)+'T'+str(time)+'_R1_bc.fq','w')
    R2outfiles[tag] = open('../split/G'+str(group)+'P'+str(patient)+'T'+str(time)+'_R2_bc.fq','w')
  else:
    R1outfiles[tag] = open('../split/G'+str(group)+'P'+str(patient)+'T'+str(time)+'_R1_bc.','w')
    R2outfiles[tag] = open('../split/G'+str(group)+'P'+str(patient)+'T'+str(time)+'_R2_bc.','w')
countfile = 0
for R1file in filenames:
  countfile += 1
  print 'working on %d file' % countfile
  R2file = R1file.replace('_R1_','_R2_')
  splitfile(R1file,R2file,R1outfiles,R2outfiles,taghash)
for tag in taghash.keys(): R1outfiles[tag].close()
for tag in taghash.keys(): R2outfiles[tag].close()
