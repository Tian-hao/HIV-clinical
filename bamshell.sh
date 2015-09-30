#!/bin/bash
REF_FILE=../ref/ref.fa
FILES=../split/*
bwa index $REF_FILE
#samtools faidx $REF_FILE
for TARGET in $FILES
do bwa mem $REF_FILE $TARGET > $TARGET.sam
done
#samtools view -bt $REF_FILE -o ../bams/$TARGET.bam ../bams/$TARGET.sam
#samtools sort -T ../tmp/$TARGET.sorted -o ../bams/$TARGET.sorted.bam ../bams/$TARGET.bam
#samtools index ../bams/$TARGET.sorted.bam
#samtools idxstats ../bams/$TARGET.sorted.bam > ../logs/$TARGET.log
#samtools mpileup -d 10000 -B -A -l ../ref/Gag_pol -f ../ref/ref.fa  -L 10000 -vuDV -o G1P1T1_R1.raw.vcf G1P1T1_R1.sorted.bam
