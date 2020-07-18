import argparse
import os
import time

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


def rlc_compression(input_string: str):
    print("[INFO] The string need encode is \n\t{}".format(input_string))
    res_string = str()

    l = len(input_string)
    i = 0

    print("[INFO] Encoding ...")
    while (i < l - 1):

        # Count the occurency of current word
        count = 1
        while (i < l and input_string[i] == input_string[i+1]):
            count += 1
            i += 1

        print("\t- The character {} occur {} times continuous..".format(input_string[i], count))
        time.sleep(0.5)

        # Append the current character with number of times it appear
        res_string = res_string + "{}:{}\n".format(input_string[i], count)
        i+= 1

    print("--> The string {} is encoded with code is {}".format({input_string}, {res_string}))
    return res_string



def rlc_decompression(encoded_string):
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
        result = rlc_compression(string)
        # Store the output data to disk
        with open(args['output'], 'w') as f:
            f.write(result)

    elif args['mode'] == 'decompression':
        rlc_decompression(string)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
