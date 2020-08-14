# The main program
import numpy as np
from config import algorithms
from utils import get_arguments, read_data
from algorithms.arithmetic_coding import get_probability_table, print_probability_table, TERMINATOR
import os
import cv2


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
        print("--> The original string is {}".format({data}))
        encoded, rcom = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=rcom)
        print("The compression ratio is {}".format(compress_ratio))
        input("Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded)

    elif args['algorithm'] == 'huffman':
        data = read_data(args['input'])
        print("--> The original string is {}".format({data}))
        (huffman_code, encoded_string) = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded_string, huffman_code=huffman_code)
        print("The compression ratio is {}".format(compress_ratio))
        input("Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded_string, huffman_code=huffman_code)

    elif args['algorithm'] == 'huffman_adap':
        data = read_data(args['input'])
        print("--> The original string is {}".format({data}))
        encoded_string = algorithm.compress(input=data)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded_string)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        input("\n[INFO] Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded_string)

    elif args['algorithm'] == 'lzw':
        data = read_data(args['input'])
        print("--> The original string is {}".format({data}))
        dictionary = []
        for i in data:
            if i not in dictionary:
                dictionary.append(i)
        dictionary.sort()
        encoded, dictionary = algorithm.compress(input=data, dictionary=dictionary)
        compress_ratio = algorithm.calculate_compression_ratio(input=data, encoded=encoded, dictionary=dictionary)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        input("\n[INFO] Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded, dictionary=dictionary)
        print("[INFO] The decoded data: {}".format(new_data.rstrip(TERMINATOR)))


    elif args['algorithm'] == 'arithmetic':
        data = read_data(args['input'])
        print("--> The original string is {}".format({data}))
        string = data.rstrip("\n") + TERMINATOR
        probability_table = get_probability_table(string)
        print_probability_table(table=probability_table)
        encoded = algorithm.compress(input=string, probability_table=probability_table)
        compress_ratio = algorithm.calculate_compression_ratio(input=string, encoded=encoded, table=probability_table)
        print("[INFO] The compression ratio is {}".format(compress_ratio))

        input("\n[INFO] Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(encoded=encoded, table=probability_table)
        print("[INFO] The decoded data: {}".format(new_data.rstrip(TERMINATOR)))

    elif args['algorithm'] == 'jpeg_lossless':
        try:
            img = cv2.imread(os.path.abspath(args['input']))
        except:
            print("The image is not found")
            exit(0)
        cv2.imshow('The origin image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        (shape, predictor, huffman_code, encoded) = algorithm.compress(
                                                        input=img, predictor=args['predictor'])
        compress_ratio = algorithm.calculate_compression_ratio(input=img, encoded=encoded)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        input("\n[INFO] Encoded the input data ... Press any key to decomress the encoded data ...")
        #new_data = algorithm.decompress(shape=shape, huffman_code=huffman_code, encoded=encoded, predictor=predictor)

    elif args['algorithm'] == 'kmean':
        try:
            img = cv2.imread(os.path.abspath(args['input']))
        except:
            print("The image is not found")
            exit(0)
        cv2.imshow('The origin image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        (shape, cluster_centers, labels) = algorithm.compress(input=img, clusters=args['clusters'])
        compress_ratio = algorithm.calculate_compression_ratio(input=img, clusters=args['clusters'])
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        input("\n[INFO] Encoded the input data ... Press any key to decomress the encoded data ...")
        new_data = algorithm.decompress(image_shape=shape,cluster_centers=cluster_centers, labels=labels)
        cv2.imshow('The origin image', new_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    args = get_arguments()
    main(args)
