import argparse
import os
import time
import numpy as np
import cv2
import pickle
from jpeg_utils import predictors
from huffman_coding import huffman_coding_compression, huffman_coding_decompression


def get_arguments():
    parser = argparse.ArgumentParser(description='The Lossless JPEG algorithm for image compression')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_losslessjpeg2.jpg',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_losslessjpeg.pl',
                        help='The output file path')
    parser.add_argument('--predictor', '-pre', default='P1',
                        choices=['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'],
                        help='The predictor')
    return vars(parser.parse_args())


def compression_ratio(input_image: np.ndarray, encoded_string: str):
    print("[INFO] Calculate the needed bits...")
    rows = input_image.shape[0]
    cols = input_image.shape[1]
    origin_bits = rows * cols * 3 * 8
    encoded_bits = len(encoded_string)
    ratio = origin_bits / encoded_bits

    print("- The number of bits needed represent image is {}".format(origin_bits))
    print("- The number of bits needed represent the ENCODED image: {}".format(encoded_bits))

    return ratio


def lossless_JPEG_Compression(image: np.ndarray, predictor:str):
    print("[INFO] Calculating the prediction matrix ...")
    prediction_matrix = predictors[predictor](image)

    print("[INFO] Calculating the different matrix ...")
    different_matrix = np.abs(image - prediction_matrix)

    # Scan the different_matrix follow the zigzag and use Huffman algorithm to encode
    print("[INFO] Scanning the different matrix ...")
    rows = image.shape[0]
    cols = image.shape[1]
    number_list = []
    for i in range(rows):
        for j in range(cols):
            number_list.append(float(different_matrix[i][j][0]))
            number_list.append(float(different_matrix[i][j][1]))
            number_list.append(float(different_matrix[i][j][2]))


    print("[INFO] Encoding the string of number by Huffman coding algorithm ...")
    huffman_code, encoded_string = huffman_coding_compression(input_string=number_list)

    return (image.shape, predictor, huffman_code, encoded_string)


def lossless_JPEG_Decompression(predictor: str, huffman_code: dict, encoded_huffman: str):

    # Huffman decoder
    print("[INFO] Decompressing the encoded by Huffman decompressor ...")

    #


def main(args):
    if args['mode'] == 'compression':
        # Read the image data from disk
        try:
            img = cv2.imread(os.path.abspath(args['input']))
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except:
            print("The image is not found")
            exit(0)

        print("[INFO] The origin image...")
        cv2.imshow('Origin image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Run the compression algorithm
        (shape, predictor, huffman_code, encoded_string) = lossless_JPEG_Compression(
                                                        image=img, predictor=args['predictor'])

        compress_ratio = compression_ratio(input_image=img, encoded_string=encoded_string)
        print("[INFO] The compression ratio is {}".format(compress_ratio))

        # Store the output data to disk
        with open(args['output'], 'wb') as f:
            pickle.dump((shape, predictor, huffman_code, encoded_string), f)

    elif args['mode'] == 'decompression':
        # Check the input file whether or not exis
        print(args['input'])
        if not os.path.isfile(args['input']):
            print("The input file is not exis")
            exit(1)

        # Read compressed data with pickle format
        with open(args['input'], 'rb') as f:
            shape, cluster_centers, labels = pickle.load(f)
            decompressed_image = k_mean_Decompression(image_shape=shape, cluster_centers=cluster_centers, labels=labels)
            print("[INFO] Display decompressed image...")
            cv2.imshow('The compressed image with {} clusters'.format(len(cluster_centers)), decompressed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    np.set_printoptions(precision=4)
    args = get_arguments()
    main(args)
