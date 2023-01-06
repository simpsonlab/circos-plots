# README

Circos is a popular tool for visualizing genomic data.  The contained
scripts provide data files and configurations for circos plots that
combine raw read counts, copy number calls and translocations.



## Usage
### calls BED
To convert a `*_calls.bed` generated from the `wf-cnv` pipeline from
ONT to usable copy number call track: 
```
python convert_bed_to_cnv_track.py --sample <sample name> --bed <full path to bed file> --type calls
```
This will generate the following output file:
```
<sample>.calls.fixed.bed
```
Note that 0 values in the call column will be removed to create
a readable circos track.

### raw BED
To convert a `*_raw_bins.bed` file, generated from the `wf-cnv`
pipeline from ONT, to a binned read depth track:
```
python convert_bed_to_cnv_track.py --sample <sample name> --bed <full path to bed file> --type raw
```
This will generate the following output file:
```
<sample>.raw.fixed.bed
```

### translocation LINK
LINK tracks in circos require a similar file format to BEDPE.
However, an additional meta data column provides a colour to
differentiate inter-chromosomal (black_a5) and intra-chromosomal
(red_a5) link lines in the circos plot:
```
python convert_bedpe_to_link.py --sample <sample name> --bedpe <full path to the translocation BEDPE file>
```
This will generate the following output file:
```
<sample>.translocation.fixed.link
```


### Snakemake
A `snakemake` pipeline has been created to simplify the process:
```
snakemake --configfile <YAML config file> -s Snakefile --cores <number of cores> all
```
This will produce all three files and can be expanded to execute circos.


### circos.example.conf
An example circos configuration file is provided in `circos.example.conf`.
Note that the `file` parameters will need to be changed.
