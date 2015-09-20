#!/bin/bash
REF_FILE=../ref/ref.fa
TARGET=G1P1T1_R1
bwa index $REF_FILE
samtools faidx $REF_FILE
bwa mem $REF_FILE ../split/$TARGET.fq > ../bams/$TARGET.sam
samtools view -bt $REF_FILE -o ../bams/$TARGET.bam ../bams/$TARGET.sam
samtools sort -T ../tmp/$TARGET.sorted -o ../bams/$TARGET.sorted.bam ../bams/$TARGET.bam
samtools index ../bams/$TARGET.sorted.bam
samtools idxstats ../bams/$TARGET.sorted.bam > ../logs/$TARGET.log
samtools mpileup -uf $REF_FILE ../bams/$TARGET.sorted.bam > ../bams/$TARGET.sorted.bcf
bcftools view ../bams/$TARGET.sorted.bcf > ../bams/$TARGET.raw.bcf 
