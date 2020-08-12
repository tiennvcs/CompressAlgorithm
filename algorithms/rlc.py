import argparse
import os
import time
from .base import Base


class RLC(Base):

    def __init__(self):
        self.name = "Run length Coding"

    def compress(self, input:str):

        input_string = input
        print("[INFO] The string need encode is \n\t{}".format(input_string))
        result = str()
        i = 0

        print("[INFO] Encoding ...")
        while i < len(input_string) - 1:

            # Count the occurrence of current word
            count = 1
            while i < len(input_string) and input_string[i] == input_string[i + 1]:
                count += 1
                i += 1

            print("\t- {} occur {} times continuous..".format(input_string[i], count))
            time.sleep(0.01)

            # Append the current character with number of times it appear
            result = result + "{}:{} ".format(input_string[i], count)
            i += 1

        print("--> The string {} is encoded with code is {}".format({input_string}, {result}))
        return result


    def decompress(self, encoded):

        encoded_string = encoded

        print("[INFO] The string need decoded is\n{}".format(encoded_string))
        count_characters = encoded_string.split(" ")
        result = ''
        print("[INFO] Decoding ...")
        for character in count_characters:
            if character == "":
                continue
            (c, count) = character.split(":")

            result += c * int(count)

            print("\tDecoded ...{}".format(c * int(count)))
            time.sleep(0.01)

        print("[INFO] The decoded string is {}".format(result))
        return result


    def calculate_compression_ratio(self, input: str, encoded: str):

        b0 = len(input)
        b1 = len(encoded)
        return b0 / b1


def get_arguments():
    parser = argparse.ArgumentParser(description='The Run Length Coding algorithms')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_rlc.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_rlc.txt',
                        help='The output file path')
    return vars(parser.parse_args())


def main(_args):
    # Check the input path is exist whether or not
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)
    # Read the text data from file
    with open(_args['input'], 'r') as f:
        string = f.read()
    # Check the mode
    rlc = RLC()
    if _args['mode'] == 'compress':
        result = rlc.compress(input_string=string)
        compress_ratio = rlc.calculate_compression_ratio(input_string=string, encoded_string=result)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'w') as f:
            f.write(result)

    elif _args['mode'] == 'decompress':
        rlc.decompress(string)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
