import argparse
import os


def get_arguments():
    parser = argparse.ArgumentParser(description='Adaptive Huffman Coding algorithms')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', required=True,
                        help='The input file path')
    parser.add_argument('--output', '-o', default="output",
                        help='The output file path')
    return vars(parser.parse_args())
