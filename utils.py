import os
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='The compression algorithms')
    parser.add_argument('--algorithm', '-al', required=True,
                        help='The compression algorithm')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', required=True,
                        help='The input file path')
    parser.add_argument('--output', '-o', required=True,
                        help='The output file path')
    return vars(parser.parse_args())
