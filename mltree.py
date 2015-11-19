#!/usr/bin/env python
import os
import sys
import glob
import string

files = sorted(glob.glob('dnds/group/G1.*ln'))
for alnfile in files:
  treefile = alnfile.rsplit('.aln')[0]+'.ph'
  treeout = alnfile.rsplit('.aln')[0]+'.out'
  wrapperfile = alnfile.rsplit('.aln')[0]+'.tmp'
  wrap = open(wrapperfile,'w')
  wrap.write(alnfile+'\nY')
  wrap.close()
  os.system('dnaml < '+wrapperfile+' >> screenout')
  os.system('mv outfile '+treeout)
  os.system('mv outtree '+treefile)
  os.system('rm '+wrapperfile)
