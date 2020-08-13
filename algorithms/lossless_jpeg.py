import argparse
import os
import time
import numpy as np
import cv2
import pickle
from .jpeg_utils import predictors
from .huffman_coding import HuffmanCoding
from .base import Base


class Lossless_JPEG(Base):

    def __init__(self):
        self.name = "Loss less JPEG compression"

    def compress(self, input: np.ndarray, predictor:str):

        image = input

        print("[INFO] Calculating the prediction matrix ...")
        prediction_matrix = predictors[predictor](image)
        print("[INFO] Calculating the different matrix ...")
        different_matrix = image - prediction_matrix

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
        huffman = HuffmanCoding()
        huffman_code, encoded_string = huffman.compress(input=number_list)
        return (image.shape, predictor, huffman_code, encoded_string)


    def decompress(self, shape, encoded: str, huffman_code: dict, predictor: str):

        # Huffman decoder
        print("[INFO] Decompressing the encoded by Huffman decompressor ...")
        huffman = HuffmanCoding()
        number_list = huffman.decompress(huffman_code=huffman_code, encoded=encoded, type_input="list")

        print("[INFO] Scaning the decoded list to construct the different matrix ...")
        different_matrix = np.empty(shape)
        rows = shape[0]
        cols = shape[1]
        count = 0
        for i in range(rows):
            for j in range(cols):
                different_matrix[i][j][0] = float(number_list[count])
                count += 1

        print("[INFO] ")



    def calculate_compression_ratio(self, input: np.ndarray, encoded: str):

        encoded_string = encoded
        input_image = input
        print("[INFO] Calculate the needed bits...")
        rows = input_image.shape[0]
        cols = input_image.shape[1]
        origin_bits = rows * cols * 3 * 8
        encoded_bits = len(encoded_string)
        ratio = origin_bits / encoded_bits

        print("- The number of bits needed represent image is {}".format(origin_bits))
        print("- The number of bits needed represent the ENCODED image: {}".format(encoded_bits))

        return ratio


def get_arguments():
    parser = argparse.ArgumentParser(description='The Lossless JPEG algorithm for image compression')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_losslessjpeg2.jpg',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_losslessjpeg.pl',
                        help='The output file path')
    parser.add_argument('--predictor', '-pre', default='P1',
                        choices=['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7'],
                        help='The predictor')
    return vars(parser.parse_args())


def main(args):
    if args['mode'] == 'compress':
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

        lossless = Lossless_JPEG()
        # Run the compression algorithm
        (shape, predictor, huffman_code, encoded_string) = lossless.compress(
                                                        input=img, predictor=args['predictor'])

        compress_ratio = lossless.calculate_compression_ratio(input=img, encoded=encoded_string)
        print("[INFO] The compression ratio is {}".format(compress_ratio))

        # Store the output data to disk
        with open(args['output'], 'wb') as f:
            pickle.dump((shape, predictor, huffman_code, encoded_string), f)

    elif args['mode'] == 'decompress':
        # Check the input file whether or not exis
        print(args['input'])
        if not os.path.isfile(args['input']):
            print("The input file is not exis")
            exit(1)

        # Read compressed data with pickle format
        with open(args['input'], 'rb') as f:
            (shape, predictor, huffman_code, encoded_string) = pickle.load(f)
            decompressed_image = lossless.decompress(shape, huffman_code, encoded, predictor)
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
