# Import encoder
from algorithms.adaptive_huffman_coding import adaptive_huffman_compression
from algorithms.huffman_coding import huffman_coding_compression
from algorithms.k_mean_clustering import k_mean_Compression
from algorithms.lossless_jpeg import lossless_JPEG_Compression
from algorithms.lzw import LZW_compression
from algorithms.rlc import rlc_compression
from algorithms.shannon_fano import shanon_FanoCompression

# Import decoder
from algorithms.adaptive_huffman_coding import adaptive_huffman_decompression
from algorithms.huffman_coding import huffman_coding_decompression
from algorithms.k_mean_clustering import k_mean_Decompression
from algorithms.lossless_jpeg import lossless_JPEG_Decompression
from algorithms.lzw import LZW_decompression
from algorithms.rlc import rlc_decompression
from algorithms.shannon_fano import shanon_FanoDecompression


algorithms = {
    'rlc': {
        'encoder': rlc_compression,
        'decoder': rlc_decompression,
    },
    'adaptive_huffman': {
        'encoder': adaptive_huffman_compression,
        'decoder': adaptive_huffman_decompression,
    },
    'huffman_coding': {
        'encoder': huffman_coding_compression,
        'decoder': huffman_coding_decompression,
    },
    'k_mean_clustering': {
        'encoder': k_mean_Compression,
        'decoder': k_mean_Decompression,
    },
    'lossless_jpeg': {
        'encoder': lossless_JPEG_Compression,
        'decoder': lossless_JPEG_Decompression,
    },
    'lzw': {
        'encoder': LZW_compression,
        'decoder': LZW_decompression,
    },
    'shannon_fano': {
        'encoder': shanon_FanoCompression,
        'decoder': shanon_FanoDecompression,
    },

}
