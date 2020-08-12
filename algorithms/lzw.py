import os
import argparse
from base import Base
import pickle


class LZW(Base):

    def __init__(self):
        self.name = "Dictionary-based Coding"

    def compress(self, input: str, dictionary):

        input_string = input
        print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|".format("Input", "Current String", "In dictionary", "Encoded Output", "Index"))
        s = ""
        res_string = []
        count = 0
        for i in input_string:
            if s + i in dictionary:
                if s == "":
                    ec_out = "nothing"
                else:
                    ec_out = "no change"
                if count == len(input_string)-1:
                    j = 0
                    while dictionary[j] != s + i:
                        j += 1
                    res_string.append(str(j))
                    ec_out = " ".join(res_string)
                s += i
                cs = s
                stb = "yes"
                index = "none"
            else:
                j = 0
                while dictionary[j] != s:
                    j += 1
                dictionary.append(s+i)
                res_string.append(str(j))

                cs = s+i
                stb = "no"
                ec_out = " ".join(res_string)
                index = len(dictionary)-1
                s = i
            count += 1
            print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|".format(input_string[0:count], cs, stb, ec_out, index))

        return (res_string, dictionary)


    def decompress(self, encoded: str, dictionary):

        encoded_string = encoded
        s = 0
        decode = ""
        count = 0
        input_copy = [int (x) for x in encoded_string.split(" ")]
        cs = dictionary[input_copy[0]]
        print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|".format("Input", "Current String", "Seen this Before ?", "Decoded Output", "Index"))
        for i in input_copy:
            de_out = dictionary[int(i)]
            decode += de_out
            cs = decode[s]
            while s < len(decode)-1:
                s += 1
                cs += decode[s]
                if cs not in dictionary:
                    dictionary.append(cs)
                    #s = s[len(s)-1]
                    break
            if len(cs) == 1:
                stb = "yes"
                index = "none"
            else:
                stb = "no"
                index = len(dictionary) - 1
            count += 1
            print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|".format(encoded_string[0: count*2], cs, stb, decode, index))
        return decode

    def calculate_compression_ratio(self, input, encoded, dictionary):
        b0 = len(input) * 8
        b1 = len(encoded) + len(dictionary)*8
        return b0 / b1


def get_arguments():
    parser = argparse.ArgumentParser(description='The Dictionary-based Coding (LZW) algorithms')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_lzw.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='output/output_lzw.pl',
                        help='The output file path')
    return vars(parser.parse_args())


def main(_args):
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)

    lzw = LZW()
    # Check the mode
    if _args['mode'] == 'compress':
        # Read the text data from file
        with open(_args['input'], 'r') as f:
            string = f.read()
        dictionary = []
        for i in string:
            if i not in dictionary:
                dictionary.append(i)
        dictionary.sort()

        dictionary, encoded = lzw.compress(input=string, dictionary=dictionary)
        compress_ratio = lzw.calculate_compression_ratio(input=string, encoded=encoded, dictionary=dictionary)

        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'wb') as f:
            pickle.dump((dictionary, encoded), f)

    elif _args['mode'] == 'decompress':
        with open(args['input'], 'rb') as f:
            dictionary, encoded_string = pickle.load(f)
        decoded_string  = lzw.decompress(encoded=encoded_string, dictionary=dictionary)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
