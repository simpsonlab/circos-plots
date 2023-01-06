import glob
import os

#
# helper functions
#
def get_raw_bed(wildcards):
    """
    Get the raw read count BED file from the config
    """
    return config['raw_bed']

def get_calls_bed(wildcards):
    """
    Get the calls BED file from the config
    """
    return config['calls_bed']

def get_translocation_file(wildcards):
    """
    Get the translocation file from the config
    """
    return config['translocation_bedpe']

def get_all_files(wildcards):
    """
    Get all the input files
    """
    files = list()
    files.append('.'.join([config['sample'], 'raw.fixed.bed']))
    files.append('.'.join([config['sample'], 'calls.fixed.bed']))
    files.append('.'.join([config['sample'], 'translocation.fixed.link']))
    return files

def get_sample_name(wildcards):
    """
    Get the sample name
    """
    return config['sample']

#
# rules
#
rule all:
    input: get_all_files


rule get_raw_bed:
    input: get_raw_bed
    output: expand("{sample}.raw.fixed.bed", sample=config['sample'])
    params:
        sample=get_sample_name,
        cmd=srcdir("convert_bed_to_cnv_track.py")
    shell:
        "python {params.cmd} --sample {params.sample} --type raw --bed {input}"

rule get_calls_bed:
    input: get_calls_bed
    output: expand("{sample}.calls.fixed.bed", sample=config['sample'])
    params:
        sample=get_sample_name,
        cmd=srcdir("convert_bed_to_cnv_track.py")
    shell:
        "python {params.cmd} --sample {params.sample} --type calls --bed {input}"

rule get_link_file:
    input: get_translocation_file
    output: expand("{sample}.translocation.fixed.link", sample=config['sample'])
    params:
        sample=get_sample_name,
        cmd=srcdir("convert_bedpe_to_link.py")
    shell:
        "python {params.cmd} --sample {params.sample} --bedpe {input}"
