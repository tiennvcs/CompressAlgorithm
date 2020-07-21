import argparse
import os


"""Adaptive Huffman coding relative function"""


# Creating tree nodes
class NodeTree(object):
    def __init__(self, parent=None, left=None, right=None, weight=0, symbol=''):
        self.parent = parent
        self.left = left
        self.right = right
        self.weight = weight
        self.symbol = symbol

    def parent(self):
        return self.parent

    def left(self):
        return self.left

    def right(self):
        return self.right

    def weight(self):
        return self.weight

    def symbol(self):
        return self.symbol


def insert_element(NYT, root, nodes, seen, str):
    node = seen[ord(str)]

    if node is None:
        spawn = NodeTree(symbol=str, weight=1)
        internal = NodeTree(symbol='', weight=1, parent=NYT.parent,
                            left=NYT, right=spawn)
        spawn.parent = internal
        NYT.parent = internal

        if internal.parent is not None:
            internal.parent.left = internal
        else:
            root = internal

        nodes.insert(0, internal)
        nodes.insert(0, spawn)

        seen[ord(str)] = spawn
        node = internal.parent

    while node is not None:
        largest = find_largest_node(nodes, node.weight)

        if (node is not largest and node is not largest.parent and
                largest is not node.parent):
            swap_node(nodes, node, largest)

        node.weight += 1
        node = node.parent

    return NYT, root, nodes, seen


def find_largest_node(nodes, weight):
    for n in reversed(nodes):
        if n.weight == weight:
            return n


def swap_node(nodes, n1, n2):
    i1, i2 = nodes.index(n1), nodes.index(n2)
    nodes[i1], nodes[i2] = nodes[i2], nodes[i1]

    tmp_parent = n1.parent
    n1.parent = n2.parent
    n2.parent = tmp_parent

    if n1.parent.left is n2:
        n1.parent.left = n1
    else:
        n1.parent.right = n1

    if n2.parent.left is n1:
        n2.parent.left = n2
    else:
        n2.parent.right = n2


def get_code(str, node, bin_string=''):
    if node.left is None and node.right is None:
        if node.symbol == str:
            return bin_string
        else:
            return ''
    else:
        temp = ''
        if node.left is not None:
            temp = get_code(str, node.left, bin_string + '0')
        if not temp and node.right is not None:
            temp = get_code(str, node.right, bin_string + '1')
        return temp


def get_symbol_by_ascii(bin_str):
    return chr(int(bin_str, 2))


def adaptive_huffman_compression(text):
    NYT = NodeTree(symbol="NYT")
    root = NYT
    nodes = []
    seen = [None] * 256

    print("[INFO] Encoding ...")

    result = ''
    for c in text:
        if seen[ord(c)]:
            result += get_code(c, root)
        else:
            result += get_code('NYT', root)
            result += bin(ord(c))[2:].zfill(8)
        # insert and update tree
        NYT, root, nodes, seen = insert_element(NYT, root, nodes, seen, c)

    print("--> The encoded with code is {}".format({result}))
    return result


def adaptive_huffman_decompression(text):
    print("[INFO] Decompressing ...")
    result = ''
    symbol = get_symbol_by_ascii(text[:8])
    result += symbol

    NYT = NodeTree(symbol="NYT")
    root = NYT
    nodes = []
    seen = [None] * 256

    NYT, root, nodes, seen = insert_element(NYT, root, nodes, seen, symbol)
    node = root

    i = 8
    while i < len(text):
        node = node.left if text[i] == '0' else node.right
        symbol = node.symbol

        if symbol:
            if symbol == 'NYT':
                symbol = get_symbol_by_ascii(text[i + 1:i + 9])
                i += 8

            result += symbol
            NYT, root, nodes, seen = insert_element(NYT, root, nodes, seen, symbol)
            node = root

        i += 1

    print("--> The decoded with code is {}".format({result}))
    return result


def compression_ratio(input_string: str, encoded_string: str):
    b0 = len(input_string) * 8
    b1 = len(encoded_string)
    return b0 / b1


"""Processing Function"""


def get_arguments():
    parser = argparse.ArgumentParser(description='Adaptive Huffman Coding algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_adaptive_huffman.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_adaptive_huffman.txt',
                        help='The output file path')
    return vars(parser.parse_args())


def main(_args):
    # Check the input path is exist whether or not
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)

    # Check the mode
    if _args['mode'] == 'compression':

        # Read the text data from file
        with open(_args['input'], 'r') as fi:
            input_string = fi.read()

        result = adaptive_huffman_compression(input_string)
        compress_ratio = compression_ratio(input_string, result)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'w') as fi:
            fi.write(result)

    elif _args['mode'] == 'decompression':

        # Read the text data from file
        with open(_args['output'], 'r') as fo:
            input_string = fo.read()

        adaptive_huffman_decompression(input_string)
    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
