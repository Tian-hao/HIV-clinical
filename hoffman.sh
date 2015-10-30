#hoffman2 scripts

qsub -cwd -V -N PJ -l h_data=4G,h_rt=24:00:00 -pe single 1 -M wunichol -m n -t 1-2:1 ~/HIVnc/myFunc2Wrapper.sh
qsub -cwd -V -N PJ -l h_data=4G,h_rt=24:00:00 -pe shared 8 -M wunichol -m n -t 3-4:1 ~/HIVnc/myFunc2Wrapper.sh
qsub -cwd -V -N PJ -l h_data=4G,h_rt=1:00:00 -M tianhao -m n -t 1-16:1 ~/HIVnc/splitWrapper.sh
qsub -cwd -V -N PJ -l h_data=4G,h_rt=1:00:00 -pe shared 8 -M tianhao -m n -t 1-16:1 ~/HIVnc/QuasiWrapper.sh
qsub -cwd -V -N PJ -l h_data=4G,h_rt=24:00:00 -pe shared 4 -M tianhao -m n -t 1-16:1 ~/HIVnc/QuasiWrapper.sh
