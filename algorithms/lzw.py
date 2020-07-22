
"""LZW relative function"""
def rlc_encode(input_string: str, dictionary):
    print("\nInput", "Current String", "In dictionary?", "Encoded Output", "Index", sep='\t\t')
    s = ""
    res_string = []
    count = 0
    for i in input_string:
        if s+i in dictionary:
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
    return ec_out

def rlc_decode(input_string: str, dictionary):
    s = 0
    decode = ""
    count = 0
    input_copy = [int (x) for x in input_string.split(" ")]
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
        print(input_string[0: count*2], cs, stb, decode, index, sep='\t\t')
    return decode

#input_string = input("Nhap chuoi: ")
input_string = "banana_bandana"

dictionary = []
for i in input_string:
    if i not in dictionary:
        dictionary.append(i)
dictionary.sort()

encode = rlc_encode(input_string, dictionary)

dictionary = []
for i in input_string:
    if i not in dictionary:
        dictionary.append(i)
dictionary.sort()

decode = rlc_decode(encode, dictionary)

print("\n", encode)
print("\n", decode)