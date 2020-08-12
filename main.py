# The main program
import numpy as np
from config import algorithms
from utils import get_arguments, read_data
import os


def main(args):
    try:
        algorithm = algorithms[args['algorithm']]
    except:
        print("The algorithm is not valid")
        exit(1)

    if not os.path.exists(args['input']):
        print("The input file is not valid !")
        exit(0)

    if args['algorithm'] == 'rlc':
        data = read_data(args['input'])
        encoded = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded)
        print("The compression ratio is {}".format(compress_ratio))
        input("Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded)

    elif args['algorithm'] == 'huffman':
        data = read_data(args['input'])
        (huffman_code, encoded_string) = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded_string)
        print("The compression ratio is {}".format(compress_ratio))
        input("Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded_string, huffman_code=huffman_code)

    elif args['algorithm'] == 'huffman_adap':
        data = read_data(args['input'])
        encoded_string = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded_string)
        print("The compression ratio is {}".format(compress_ratio))
        input("Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded_string)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
