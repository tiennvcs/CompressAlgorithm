import argparse
import os
import time


"""RLC relative function"""


def compression_ratio(input_string: str, encoded_string: str):
    b0 = len(input_string)
    b1 = len(encoded_string)
    return b0 / b1


def rlc_Compression(input_string: str):
    print("[INFO] The string need encode is \n\t{}".format(input_string))
    res_string = str()
    l = len(input_string)
    i = 0

    print("[INFO] Encoding ...")
    while i < l - 1:

        # Count the occurrence of current word
        count = 1
        while i < l and input_string[i] == input_string[i + 1]:
            count += 1
            i += 1

        print("\t- {} occur {} times continuous..".format(input_string[i], count))
        time.sleep(0.5)

        # Append the current character with number of times it appear
        res_string = res_string + "{}{}".format(input_string[i], count)
        i += 1

    print("--> The string {} is encoded with code is {}".format({input_string}, {res_string}))
    return res_string


def rlc_Decompression(encoded_string):
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


"""Processing Function"""


def get_arguments():
    parser = argparse.ArgumentParser(description='The Run Length Coding algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
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
    if _args['mode'] == 'compression':
        result = rlc_Compression(input_string=string)
        compress_ratio = compression_ratio(input_string=string, encoded_string=result)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'w') as f:
            f.write(result)

    elif _args['mode'] == 'decompression':
        rlc_Decompression(string)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
