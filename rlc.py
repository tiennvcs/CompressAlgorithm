import argparse
import os

def get_arguments():
    parser = argparse.ArgumentParser(description='The Run Length Coding algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='input/input_rlc.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='output/output.txt',
                        help='The output file path')
    return vars(parser.parse_args())

def rlc_compression():
    pass

def rlc_decompression():
    pass

def main(args):
    # Check the input path is exis whether or not
    if not os.path.isfile(args['input']):
        print("The input file is not exis")
        exit(1)
    # Read the text data from file

    # Check the mode
    if args['mode'] == 'compression':
        rlc_compression()
    elif args['mode'] == 'decompression':
        rlc_decompression()
    else:
        print("The selected mode is not valid")
        exit(0)

    # Store the output data to disk


if __name__ == '__main__':
    args = get_arguments()
    main(args)
