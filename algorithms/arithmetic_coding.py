import argparse
import os
import pickle
import string
import sys
import time
from .base import Base

TERMINATOR = "$"

def float_bin(number, places=12):
    whole, des = str(number).split(".")
    res = bin(int(whole)).split("b")[1]
    des = number - int(whole)
    res = ""
    remain_stores = set()
    while (des != int(des)):
        des = des * 2
        res += str(int(des) % 2)
        if int(des) >= 2:
            des -= 2
    return res


def bin_float(string: str):
    whole, dec = string.split(".")
    res = 0
    k = -1
    for digit in dec:
        res += int(digit) * 2**k
        k -= 1
    return res


def get_probability_table(infomation_source):

    count_frequencies = dict()
    table = dict()

    for value in infomation_source:
        if value in count_frequencies:
            count_frequencies[value] += 1
        else:
            count_frequencies[value] = 1

    count_sum = len(infomation_source)

    low_prob = 0

    for key in count_frequencies:
        range = count_frequencies[key] / count_sum
        table[key] = (low_prob, low_prob + range)
        low_prob = low_prob + range

    return table


def print_probability_table(table):
    print("The probability table of each symbol.")
    print("|{:<10}|{:<30}|".format("Symbol", "Range"))
    print("-"*43)
    for key in table:
        print(r"""|{:<10}|{:<30}|""".format(str(key), "[{}, {})".format(round(table[key][0], 10), round(table[key][1], 10))))
    print("-"*43)


class Arithmetic(Base):

    def __init__(self):
        self.name = "Arithmetic coding"

    def compress(self, input: str, probability_table):

        input_string = input
        print("[INFO] Compressing ...")
        low = 0.0
        high = 1.0
        range = 1.0

        print("{:>10}|{:>20}|{:>20}|{:>20}".format("Symbol", "Low", "High", "Range"))
        print("-"*73)

        for symbol in input_string:
            new_low = low + range * probability_table[symbol][0]
            new_high = low + range * probability_table[symbol][1]

            low = round(new_low, 10)
            high = round(new_high, 10)
            range = round(high - low, 10)
            #print("{:>10}|{:>20}|{:>20}|{:>20}".format(symbol, low, high, range))

        print("-"*73)

        # Get the middle value in range [low, high] to encode
        value = round(low + (high-low)/2, 10)
        print("[INFO] The value encoded: {}".format(value))
        time.sleep(1)

        bin_value = "0." + float_bin(value)
        print("[INFO] The binary representation of bellow value: {}".format(bin_value))
        time.sleep(1)

        return bin_value


    def decompress(self, encoded: str, table):

        value = round(bin_float(encoded), 10)
        print("[INFO] The value decoded from the binary string: {}".format(value))

        low = 0
        high = 1.0
        range = 1.0
        res = ""
        symbol = ""
        print("[INFO] Decompresing ...\n")

        print("{:<12}|{:<20}|{:<20}|{:<20}|{:<20}".format("Value", "Output symbol", "Low", "High", "Range"))
        print("-"*92)

        while symbol != TERMINATOR:

            # Find the symbol s that probability_table[s][0] <= code < probability_table[s][1]
            for key in table:
                if table[key][0] <= value < table[key][1]:
                    symbol = key
                    break
            low = round(table[symbol][0],10)
            high = round(table[symbol][1], 10)
            range = round(high - low, 10)

            print("{:<12}|{:<20}|{:<20}|{:<20}|{:<20}".format(value, symbol, low, high, range))
            time.sleep(0.2)

            res += symbol

            value = round((value - low) / range, 10)

        print("-"*92)
        return res


    def calculate_compression_ratio(self, input: str, encoded: float, table: dict):
        b0 = sys.getsizeof(input) * 8   # bits
        b1 = len(encoded) + len(table) * 40  # bits
        return b0 / b1


def get_arguments():
    parser = argparse.ArgumentParser(description='The Aritmetic compression algorithms')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
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

    arithmetic = Arithmetic()

    if _args['mode'] == 'compress':
        # Read the text data from file
        with open(_args['input'], 'r') as f:
            string = f.read().rstrip("\n")
            # Add the terminator at the end of string
            string += TERMINATOR

        probability_table = get_probability_table(string)
        print_probability_table(table=probability_table)

        encoded = arithmetic.compress(input=string, probability_table=probability_table)

        compress_ratio = arithmetic.calculate_compression_ratio(input=string, encoded=encoded, table=probability_table)

        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'wb') as f:
            pickle.dump((encoded, probability_table), f)

    elif _args['mode'] == 'decompress':
        with open(_args['input'], 'rb') as f:
            (encoded, probability_table) = pickle.load(f)
        print("The encoded binary string: {}".format(encoded))
        decoded_string = arithmetic.decompress(encoded=str(encoded), table=probability_table)
        print("[INFO] The decoded string: {}".format(decoded_string))
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
