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
    description = 'Convert a BEDPE file to a link file that can be used with circos'
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument('-s', '--sample', required=True,
            help='name of the sample being processed')
    parser.add_argument('-b', '--bedpe', required=True,
            help='BEDPE file containing translocations')
    return parser.parse_args()


def main():
    """
    Main program
    """
    args = init_args()
    tx_colname = ['chrA', 'startA', 'endA', 'chrB', 'startB', 'endB', 'val1', 'val2']
    is_intra = False
    output_file = f'{args.sample}.translocation.fixed.link'
    ofh = open(output_file, 'w')
    with open(args.bedpe, 'r') as tx:
        reader = csv.DictReader(tx, fieldnames=tx_colname, delimiter='\t')
        for line in reader:
            if line['chrA'].startswith('chr'):
                line['chrA'] = re.sub('chr', 'hs', line['chrA'])
            if line['chrB'].startswith('chr'):
                line['chrB'] = re.sub('chr', 'hs', line['chrB'])
            if re.search(',', line['chrB']):
                continue
            if line['chrA'] == line['chrB']:
                is_intra = True
            if is_intra:
                line_color = "color=red_a5"
            else:
                line_color = "color=black_a5"
            ofh.write('\t'.join([
                line['chrA'],
                line['startA'],
                line['endA'],
                line['chrB'],
                line['startB'],
                line['endB'],
                line_color]))
            ofh.write('\n')
    ofh.close()


if __name__ == '__main__':
    main()


#__END__

