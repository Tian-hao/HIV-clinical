#!/usr/bin/env python
#sam to mutation count
#sam to mutation frequency
#and sam to consensus
from __future__ import division
import os
import re
import sys
import glob
import string
from Bio import SeqIO

path2sam = '../errorcorrection/'
path2freq= '../freq/'
path2tmp = '../tmp/'
samfiles = sorted(glob.glob(path2sam+'*.sam'))
reffile  = open('../ref/ref.fa','r')
cnshandle= open(path2freq+'consensus.fa','w')
refhandle= SeqIO.parse(reffile,'fasta')
for record in refhandle:
  refseq = record.seq
for samfile in samfiles:
  samname  = samfile.rsplit(path2sam)[1].rsplit('.sam')[0] 
  bamfile  = path2tmp+samname+'.bam'
  jsonfile = path2tmp+samname+'.json'
  countfile= path2freq+samname+'.count'
  freqfile = path2freq+samname+'.freq'
  cnsfile  = path2freq+samname+'.cns.fa'
  os.system('samtools view -bS '+samfile+' > '+bamfile)
  os.system('bamtools convert -format json -in '+bamfile+' -out '+jsonfile)
  inhandle = open(jsonfile,'r')
  counthandle = open(countfile,'w')
  freqhandle  = open(freqfile,'w')
  count = {}
  for i in range(0,1520):
    for base in ['A','T','C','G']:
      count[base+str(i)] = 0
  for line in inhandle.xreadlines():
    line = line.rstrip()
    info = line.rsplit('"')
    if '["113M"]' in line:
      startsite = info[14][1:-1]
      JsonMut = info[int(info.index('MD'))+2]
      Seq = info[int(info.index('queryBases'))+2]
      if 'N' in Seq: continue
      inpos = 1000
      MutPos = re.findall('\d+',JsonMut)
      wtbase = JsonMut.translate(None,'1234567890')
      MutPosarray = []
      MutIDarray = []
      RefPosarray = []
      RefPos = int(startsite)-1
      for i in range(RefPos, RefPos+113):
        count[refseq[i]+str(i)] += 1
      Pos = 0
      for i in range(0,len(MutPos)-1):
        RefPos = RefPos + int(MutPos[i]) + 1
        Pos = Pos + int(MutPos[i]) + 1
        RefPosarray.append(RefPos)
        MutPosarray.append(Pos)
      for i in range(0,len(MutPosarray)):
        mutbase = Seq[MutPosarray[i]-1]
        RefPosOut = RefPosarray[i]
        if MutPosarray[i] >= inpos:
          RefPosOut = RefPosOut + 1
	count[wtbase[i]+str(RefPosOut-1)] -= 1
	count[mutbase+str(RefPosOut-1)] += 1
  CNS = ''
  for i in range(0,1520):
    countA = count['A'+str(i)]
    countT = count['T'+str(i)]
    countC = count['C'+str(i)]
    countG = count['G'+str(i)]
    countall = countA + countT + countC + countG
    if countall == 0: countall = 1
    counthandle.write(str(i)+'\t'+str(countA)+'\t'+str(countT)+'\t'+str(countC)+'\t'+str(countG)+'\n')
    freqhandle.write(str(i)+'\t'+str(countA/countall)+'\t'+str(countT/countall)+'\t'+str(countC/countall)+'\t'+str(countG/countall)+'\n')
    if countA>countT and countA>countC and countA>countG: CNS += 'A'
    elif countT>countA and countT>countC and countT>countG: CNS += 'T'
    elif countC>countT and countC>countA and countC>countG: CNS += 'C'
    elif countG>countT and countG>countC and countG>countA: CNS += 'G'
    else: CNS += 'N'
  cnshandle.write('>'+samname+'\n')
  cnshandle.write(CNS+'\n')

        
        


