import os
import argparse


def LZW_compression(input_string: str, dictionary):
    print("\nInput", "Current String", "In dictionary?", "Encoded Output", "Index", sep='\t\t')
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
        print(input_string[0:count], cs, stb, ec_out, index, sep='\t\t')
    return (res_string, dictionary)


def LZW_decompression(encoded_string: str, dictionary):
    s = 0
    decode = ""
    count = 0
    input_copy = [int (x) for x in encoded_string.split(" ")]
    cs = dictionary[input_copy[0]]
    print("\nInput", "Current String", "Seen this Before?", "Decoded Output", "Index", sep='\t\t')
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
        print(encoded_string[0: count*2], cs, stb, decode, index, sep='\t\t')
    return decode


def get_arguments():
    parser = argparse.ArgumentParser(description='The Dictionary-based Coding (LZW) algorithms')
    parser.add_argument('--mode', '-m', default='compression',
                        choices=['compression', 'decompression'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_rlc.txt',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_rlc.txt',
                        help='The output file path')
    return vars(parser.parse_args())

    
def main(args):
    if not os.path.isfile(_args['input']):
        print("The input file is not exist")
        exit(1)

    # Check the mode
    if _args['mode'] == 'compression':
        # Read the text data from file
        with open(_args['input'], 'r') as f:
            string = f.read()
        dictionary = []
        for i in input_string:
            if i not in dictionary:
                dictionary.append(i)
        dictionary.sort()

        dictionary, encoded = LZW_compresion(input_string=string, dictionary=dictionary)

        compress_ratio = compression_ratio(input_string=string, encoded_string=result)
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(_args['output'], 'w') as f:
            f.write(encoed)
    elif _args['mode'] == 'decompression':
        with open(args['input'], 'rb') as f:
            dictionary, encoded_string = pickle.load(f)

        decoded_string  = LZW_decompression(encoded_string=encoded_string, dictionary=dictionary)

    else:
        print("The selected mode is not valid")
        exit(0)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
