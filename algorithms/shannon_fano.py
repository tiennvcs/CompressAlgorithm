import argparse
import os
import time
from collections import Counter
from .base import Base

class ShanonFano(Base):
    def __init__(self):
        self.name = "Shanon Fano algorithm"

    def compress(self, input: str):

        input_string = input

        print("[INFO] The string need encoded is \n\t{}".format(input_string))

        # Count the frequency of the symbols in input_string
        print("[INFO] Counting the frequency of symbols in string ...")
        frequency_count = Counter(sorted(input_string))
        del frequency_count['\n']
        time.sleep(1)

        # Sort the frequency_count ascending.
        sorted_counts = {k: v for k, v in sorted(frequency_count.items(), key=lambda item: item[1])}

    def decompress(self, encoded):

        encoded_string = encoded

        res_string = ""

        print("[INFO] The string need decoded is\n{}".format(encoded_string))
        count_characters = encoded_string.split("\n")

        print("[INFO] Decoding ...")
        for character in count_characters:
            if character == "":
                continue
            (c, count) = character.split(":")

            res_string += c * int(count)

            print("\tDecoded ...{}".format(c * int(count)))
            time.sleep(1)

        print("[INFO] The decoded string is {}".format(res_string))
        return res_string

    def calculate_compression_ratio(self, input, encoded, dictionary):
        b0 = len(input)*8
        b1 = len(encoded) + len(dictionary)*40
        return b0 / b1
        

def get_arguments():
    parser = argparse.ArgumentParser(description='The Shannon-Fano algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_shanon-fano.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_shanon-fano.txt',
                        help='The output file path')
    return vars(parser.parse_args())


def main(args):
    # Check the input path is exis whether or not
    if not os.path.isfile(args['input']):
        print("The input file is not exis")
        exit(1)
    # Read the text data from file
    with open(args['input'], 'r') as f:
        string = f.read()
    # Check the mode
    if args['mode'] == 'compression':
        result = shanon_FanoCompression(string)
        # Store the output data to disk
        with open(args['output'], 'w') as f:
            f.write(result)

    elif args['mode'] == 'decompression':
        shanon_FanoDecompression(string)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
