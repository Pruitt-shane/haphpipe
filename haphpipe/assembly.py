#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from utils.sysutils import args_params

import stages
from stages import trim_reads
from stages import join_reads
from stages import ec_reads
from stages import assemble_denovo
# from stages import assign_contigs
from stages import assemble_scaffold
from stages import assemble_amplicons
# from stages import impute_ref
from stages import align_reads
from stages import call_variants
from stages import refine_assembly
from stages import fix_consensus
from stages import pairwise_align
from stages import vcf_to_fasta
from stages import post_assembly
from stages import extract_pairwise
from stages import annotate_from_ref

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(help='Assembly stages')
    trim_reads.stageparser(sub.add_parser('trim_reads'))
    join_reads.stageparser(sub.add_parser('join_reads'))    
    ec_reads.stageparser(sub.add_parser('ec_reads'))
    assemble_denovo.stageparser(sub.add_parser('assemble_denovo'))
    # assign_contigs.stageparser(sub.add_parser('assign_contigs'))
    assemble_scaffold.stageparser(sub.add_parser('assemble_scaffold'))
    # impute_ref.stageparser(sub.add_parser('impute_ref'))
    assemble_amplicons.stageparser(sub.add_parser('assemble_amplicons'))
    refine_assembly.stageparser(sub.add_parser('refine_assembly'))
    align_reads.stageparser(sub.add_parser('align_reads'))
    call_variants.stageparser(sub.add_parser('call_variants'))
    pairwise_align.stageparser(sub.add_parser('pairwise_align'))    
    fix_consensus.stageparser(sub.add_parser('fix_consensus'))
    vcf_to_fasta.stageparser(sub.add_parser('vcf_to_fasta'))
    
    post_assembly.stageparser(sub.add_parser('post_assembly'))
    extract_pairwise.stageparser(sub.add_parser('extract_pairwise'))
    annotate_from_ref.stageparser(sub.add_parser('annotate_from_ref'))
    
    args = parser.parse_args()
    args.func(**args_params(args))

if __name__ == '__main__':
    main()
