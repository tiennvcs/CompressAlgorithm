import argparse
import os
from collections import Counter
import pickle


"""Aritmetic algorithm"""

def aritmetic_Compression(input_string: object):
    pass


def arithmetic_Decompression(huffman_code: dict, encoded_string: str, type_input="str"):
    pass


def compression_ratio(input_string: str, encoded_string: str):
    return 0


"""Processing Function"""


def get_arguments():
    parser = argparse.ArgumentParser(description='The Aritmetic compression algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_arithmetic.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_arithmetic.pl',
                        help='The output file path')
    return vars(parser.parse_args())

def main(_args):
    # Check the input path is exist whether or not
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)

    if _args['mode'] == 'compression':
        # Read the text data from file
        with open(_args['input'], 'r') as f:
            string = f.read()

        aritmetic_Compression(string)
        print(string)
        # compress_ratio = compression_ratio(input_string=string, encoded_string=encoded_string)
        # print("[INFO] The compression ratio is {}".format(compress_ratio))
        # # Store the output data to disk
        # with open(_args['output'], 'wb') as f:
        #     pickle.dump((huffman_code, encoded_string), f)

    elif _args['mode'] == 'decompression':
        with open(_args['input'], 'rb') as f:
            (huffman_code, encoded_string) = pickle.load(f)
        huffman_coding_decompression(huffman_code=huffman_code, encoded_string=encoded_string)

    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
