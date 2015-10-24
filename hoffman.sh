#hoffman2 scripts

qsub -cwd -V -N PJ -l h_data=1024M,h_rt=01:00:00 -M wunichol -m n -t 1-7:1 ~/HIVnc/myFunc2Wrapper.sh
