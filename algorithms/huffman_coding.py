import argparse
import os
from collections import Counter
import pickle
from .base import Base

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, bin_string=''):
    if type(node) is float or type(node) is str:
        return {node: bin_string}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, bin_string + '0'))
    d.update(huffman_code_tree(r, bin_string + '1'))
    return d


class HuffmanCoding(Base):

    def __init__(self):
        self.name = "Huffman Coding"

    def compress(self, input: object):

        input_string = input
        print("\n[INFO] Encoding ...")
        # Calculating frequency
        freq = dict(Counter(input_string))
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        nodes = freq

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffman_code = huffman_code_tree(nodes[0][0])

        output_freq = ' Char | Huffman code \n'
        for (char, frequency) in freq:
            output_freq = output_freq + ('%r | %s' % (char, huffman_code[char])) + '\n'
        encoded_string = ''
        for char in input_string:
            encoded_string += huffman_code[char]

        print(output_freq)

        print("--> The encoded with code is {}".format({encoded_string}))
        return huffman_code, encoded_string


    def decompress(self, encoded: str, huffman_code: dict, type_input="str"):
        encoded_string = encoded
        print("\n[INFO] Decompressing ...")
        key_list = list(huffman_code.keys())
        val_list = list(huffman_code.values())
        s = ''
        if type_input == "str":
            result = ''
            for char in encoded_string:
                s += char
                if s in val_list:
                    result += str(key_list[val_list.index(s)])
                    s = ''
        else:
            result = []
            for char in encoded_string:
                s += char
                if s in val_list:
                    result.append(key_list[val_list.index(s)])
                    s = ''

        print("--> The decoded with code is {}".format({result}))
        return result


    def calculate_compression_ratio(self, input: str, encoded: str, huffman_code):
        b0 = len(input) * 8
        b1 = len(encoded)
        return b0 / b1


def get_arguments():
    parser = argparse.ArgumentParser(description='The Huffman Coding algorithms')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_huffman.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_huffman.pl',
                        help='The output file path')
    return vars(parser.parse_args())


def main(_args):
    # Check the input path is exist whether or not
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)

    huffman = HuffmanCoding()

    if _args['mode'] == 'compress':
        # Read the text data from file
        with open(_args['input'], 'r') as f:
            string = f.read()

        (huffman_code, encoded_string) = huffman.compress(input=string)
        compress_ratio = huffman.calculate_compression_ratio(input=string, encoded=encoded_string)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'wb') as f:
            pickle.dump((huffman_code, encoded_string), f)

    elif _args['mode'] == 'decompress':
        with open(_args['input'], 'rb') as f:
            (huffman_code, encoded_string) = pickle.load(f)
            print(huffman_code)
            print(encoded_string)
            input()
        huffman.decompress(encoded=encoded_string, huffman_code=huffman_code)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
