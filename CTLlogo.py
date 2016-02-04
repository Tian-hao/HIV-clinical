#!/usr/bin/env python
import os
import sys
import glob
import string

fastafiles = sorted(glob.glob('../freq/ctl/sampling/*.fa'))
for fasfile in fastafiles:
  logofile = '../freq/ctl/logo/'+fasfile.rsplit('sampling/')[1].rsplit('.fa')[0]+'.png'
  os.system('weblogo -f '+fasfile+' -o '+logofile+' -F png')
