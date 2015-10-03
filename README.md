# HIV-clinical
 The scripts for some innate immune response HIV-clinical samples.

 #############
 split.py is for splitting NGS files into sample files. It needs a tag file.
 mapping.py uses bwa to align NGS reads onto Gag_pol, outputs haplotype on every read.
 pairing.py aligns the haplotype of paired reads. It outputs haplotypes.
 countmutation.py counts haplotypes and outputs mutation frequencies.
