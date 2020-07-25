from collections import Counter


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_code_tree(node, left=True, binString=''):
    if type(node) is int:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def huffman_coding_compression(input_list):
    print("[INFO] Encoding ...")
    # Calculating frequency
    freq = dict(Counter(input_list))
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
    for char in input_list:
        encoded_string += huffman_code[char]
    print(output_freq)
    print(encoded_string)

    return huffman_code, encoded_string


def huffman_coding_decompression(encoded_string: str, huffman_code):
    print("[INFO] Decompressing ...")
    key_list = list(huffman_code.keys())
    val_list = list(huffman_code.values())
    res_string = []
    s = ''
    for char in encoded_string:
        s += char
        if s in val_list:
            res_string.append(key_list[val_list.index(s)])
            s = ''
    print('Output:')
    print(res_string)
    return res_string


#huf, end = huffman_coding_compression([12, 12, 12, 24, 12, 24, 100, 0, 0, 0, 0, 10])
huf, end = huffman_coding_compression("ABCCCCCBBBDDAAA")

huffman_coding_decompression(end, huf)
