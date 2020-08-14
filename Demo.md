# DEMO
Chạy các lệnh bên dưới trên Terminal để thực hiện demo
## CÁC THUẬT TOÁN NÉN VĂN BẢN
### RLC
```bash
python main.py -al rlc -i input/input_rlc.txt
```
### Huffman Coding
```bash
python main.py -al huffman -i input/input_huffman.txt
```
### Adaptive Huffman Coding
```bash
python main.py -al huffman_adap -i input/input_adaptive_huffman.txt
```
### Dictionary-based Coding
```bash
python main.py -al lzw -i input/input_lzw.txt
```
### Arithmetic Coding
```bash
python main.py -al arithmetic -i input/input_arithmetic.txt
```
## CÁC THUẬT TOÁN NÉN ẢNH

### JPEG lossless
```bash
python main.py -al jpeg_lossless -i input/input_losslessjpeg.jpg
```
### K-mean clustering (K=32)
```bash
python main.py -al kmean -i input/input_losslessjpeg1.jpg --clusters 16
```
### K-mean clustering (K=64)
```bash
python main.py -al kmean -i input/input_losslessjpeg1.jpg --clusters 32
```
