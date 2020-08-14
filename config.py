from algorithms.rlc import RLC
from algorithms.huffman_coding import HuffmanCoding
from algorithms.adaptive_huffman_coding import HuffmanCodingAdaptive
from algorithms.arithmetic_coding import Arithmetic
from algorithms.lossless_jpeg import Lossless_JPEG
from algorithms.k_mean_clustering import Kmean
from algorithms.lzw import LZW

algorithms = {
    'rlc': RLC(),
    'lzw': LZW(),
    'huffman': HuffmanCoding(),
    'huffman_adap': HuffmanCodingAdaptive(),
    'arithmetic': Arithmetic(),
    'jpeg_lossless': Lossless_JPEG(),
    'kmean': Kmean()
}
