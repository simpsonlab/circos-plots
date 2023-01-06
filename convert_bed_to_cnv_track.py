#!/usr/bin/env python

import csv
import re
import os
import sys
import argparse


def init_args():
    """
    Initialize command line arguments
    """
    description = 'Convert a BED file to a cnv track file that can be used with circos'
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument('-s', '--sample', required=True,
            help='name of the sample being processed')
    parser.add_argument('-b', '--bed', required=True,
            help='BED file containing copy number data')
    parser.add_argument('-t', '--type', required=False, default='raw',
            help='type of BED data in the input file, must be either raw or calls')
    return parser.parse_args()


def main():
    """
    Main program
    """
    args = init_args()
    tx_colname = ['chr', 'start', 'end', 'region', 'score', 'strand']
    is_intra = False
    output_file = f'{args.sample}.{args.type}.fixed.bed'
    ofh = open(output_file, 'w')
    if args.type == 'calls':
        is_calls = True
    else:
        is_calls = False
    with open(args.bed, 'r') as tx:
        reader = csv.DictReader(tx, fieldnames=tx_colname, delimiter='\t')
        for line in reader:
            # skip the BED "tracklayer" meta data line
            if line['chr'].startswith('track'):
                continue
            if not line['chr'].startswith('chr'):
                line['chr'] = re.sub('^', 'hs', line['chr'])
            if is_calls and line['score'] == '0':
                continue
            ofh.write('\t'.join([
                line['chr'],
                line['start'],
                line['end'],
                line['score']]))
            ofh.write('\n')
    ofh.close()



if __name__ == '__main__':
    main()


#__END__

