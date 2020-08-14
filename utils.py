import os
import argparse

def read_data(path_file):
    if path_file.endswith(".txt"):
        with open(path_file, 'r', encoding='utf8') as f:
            data = f.read()
    elif path_file.endswith(".png") or path_file.endswith(".jpeg"):
        data = cv2.imread(path_file)

    return data


def get_arguments():
    parser = argparse.ArgumentParser(description='The compression algorithms')
    parser.add_argument('--algorithm', '-al', required=True,
                        choices=["rlc", "lzw", "huffman", "huffman_adap", "arithmetic", "jpeg_lossless", "kmean"],
                        help='The compression algorithm')
    parser.add_argument('--input', '-i', required=True,
                        help='The input file path')
    parser.add_argument('--output', '-o', default="output",
                        help='The output file path')
    parser.add_argument("--predictor", '-pre', default="P1",
                        help="The predictor for JPEG lossless algorithm")
    parser.add_argument('--clusters', '-k', default=8, choices=[4, 8, 16, 32, 64, 128],
                        type=int, help='The number of clusters')
    return vars(parser.parse_args())
