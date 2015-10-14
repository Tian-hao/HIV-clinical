# HIV-clinical
 The scripts for some innate immune response HIV-clinical samples.

 #############
 split.py is for splitting NGS files into sample files. It needs a tag file.
 mapping.py uses bwa to align NGS reads onto Gag_pol, outputs haplotype on every read.
 pairing.py aligns the haplotype of paired reads. It outputs haplotypes.
 countmutation.py counts haplotypes and outputs mutation frequencies.

 #############

 2015.10.13

 R code is annotated independently.

 pipeline1:

 split.py is for splitting NGS files into sample files, according to 3 nucleotide tag. A tag file is needed.

 a split -l LINES sentence is needed before next step.

 mapping.py uses bwa aln and bwa sampe to map NGS reads onto Gag, it gives sam and bam output. This script is from Nicholas C. Wu

 sam2mutation.py count the mutation number and mutation frequency from sam input. It also give consensus sequence output.

 This pipeline cannot gain information on haplotypes.

 pipeline2:

 split.py is for splitting NGS files into sample files, according to 3 nucleotide tag. A tag file is needed.

 a split -l LINES sentence is needed before next step.

 mapping.py uses bwa aln and bwa sampe to map NGS reads onto Gag, it gives sam and bam output. This script is from Nicholas C. Wu

 pairing.py align uses haplotype output from mapping.py as input. It generates haplotype format. This is also from Nicholas C. Wu

 haplo2mutation.py count the mutation frequency.

 This pipeline is not sufficient to reconstruct haplotype.
