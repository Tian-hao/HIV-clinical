#!/usr/bin/env python
import os
import sys
import glob
import string

pathdata = '/media/Yushen/split/'
pathbam  = '/media/Yushen/bams/'
pathtmp  = '../tmp/'
refseq   = '../ref.fa'
fqfiles  = sorted(glob.glob(pathdata+'*_R1.fq'))
for fqfile1 in fqfiles:
  fqfile2  = fqfile1.replace('_R1','_R2')
  fqfile   = fqfile1.rsplit('_')[0].rsplit(pathdata)[1]
  if os.path.getsize(fqfile1) > 1000000000: 
    os.system("split -l 15000000 "+fqfile1+" "+fqfile+"_R1")
    os.system("split -l 15000000 "+fqfile2+" "+fqfile+"_R2")
    os.system("rm "+fqfile1)
    os.system("rm "+fqfile2)
fqfiles  = sorted(glob.glob(pathdata+'*.fq')
for fqfile in fqfiles:
  newname = fqfile.rsplit('.fq')[0]+'aa'
  os.system("mv "+fqfile+" "+newname)
fqfiles  = sorted(glob.glob(pathdata+"*_R1a")
for fqfile1 in fqfiles:
  fqfile2  = fqfile1.replace('R1','R2')
  saifile1 = pathbam+fqfile1.rsplit(pathdata)[1]+'.sai'
  saifile2 = pathbam+fqfile2.rsplit(pathdata)[1]+'.sai'
  fqfile   = fqfile1.rsplit('R1')[0]+fqfile1.rsplit('R1')[1]
  samfile  = pathbam+fqfile.rsplit(pathdata)[1]+'.sam'
  bamfile  = samfile.rsplit('.sam')[0]+'.bam'
  tmpfile  = pathtmp+fqfile.rsplit(pathdata)[1]+'.sort'
  sortbam  = bamfile.rsplit('.bam')[0]+'sorted.bam'
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile1+" > "+saifile1)
  os.system("bwa aln -B 4 -l 7 -k 2 -n 8 "+refseq+" "+fqfile2+" > "+saifile2)
  os.system("bwa sampe "+refseq+" "+saifile1+" "+saifile2+" "+fqfile1+" "+fqfile2+" > "+samfile)
  os.system("rm "+saifile1)
  os.system("rm "+saifile2)
  os.system("samtools view -bS "+samfile+" > "+bamfile)
  os.system("samtools sort -T "+tmpfile+" "+bamfile+" > "+sortbam)

