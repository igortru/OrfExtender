#!/usr/bin/python
import sys

###############################################################################
# 
# Author:
#
# Sanyk28 (san-heng-yi-shu@163.com)
#
# Date created:
#
# 12 June 2013
#
# Rosalind problem:
#
# Open Reading Frames
# 
# Given: A DNA string s of length at most 1 kbp in FASTA format
# 
# Return: Every distinct candidate protein string that can be translated from ORFs 
#         of s. Strings can be returned in any order
#
# Usage:
#
# python ORF.py [Input File]
#
################################################################################

import sys
import re

DNA_CODON = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': '*',     'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': '*',     'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': '*',     'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

M_CODON = {'GTG' : 'M', 'ATG' : 'M', 'TTG' : 'M'}
#, 'CTG' : 'M', 'ATT' : 'M', 'ATC' : 'M'}

def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON:
        protein = DNA_CODON[codon]
    return protein

# generate sub_seqs according to start codons
def sub_seqs(seq):
    sub_seq = []
    sub_seq.append(re.findall('...',seq))
    return sub_seq

# translate DNA to protein
def translation(seq):
    protein = ""
    for sub_seq in sub_seqs(seq):
        for codon in sub_seq:
                if len(protein) == 0  and codon in M_CODON:
                    protein += M_CODON[codon]
                else:
                    protein += translate_codon(codon)
    return protein

