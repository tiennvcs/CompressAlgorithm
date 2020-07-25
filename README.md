# Implement of some data compression algorithm

## Description
----

Data compression is one of the most important when we need store and transmit data, such as text, image, video.

The project will implement common compression and decompression algorithm using Python programming language, includes:

- Run Length Coding (RLC).

- Variable Length Coding (VLC, includes:

	+ Shannon-Fano Algorithm (top-down approach).

	+ Huffman Coding Algorithm(bottom-up approach).

	+ Extended Huffman Coding.

	+ Adaptive Huffman Coding (stream data).

- Dictionary-base Coding (LZW).

- Arithmetic Coding.

- Lossless JPEG (for image).

- Lossy JPEG (for image).

- k-mean clustering (for image).


*Note: the data for Lossless, Lossy JPEG, k-mean clustering compression is image, the other algorithms use text instead.*

## Usage
----

Example for compression the data in file with name *fileinput* using Run Length Coding algorithm.

```bash
python algorithms/rlc.py --mode *compression* --input *fileinput* --output *fileoutput*
```

*If you want to decomrpess the information change the option **mode** to **decompression** and given the suitable arguments*.

## Evaluate the algorithms

| Algorithm                                     	| Perspective 	| Pros 	| Cons 	|
|-----------------------------------------------	|-------------	|------	|------	|
| Run Length Coding                             	| Count the number of times the occurency's current character.            	| if the information source has the property that symbols tend to form continuous groups, then such symbol and the length of the group can be coded.     	|      	|
| <strike>Shannon-Fano Algorithm (top-down approach)</strike>    	|             	|      	|      	|
| Huffman Coding Algorithm (bottom-up approach) 	| Huffman Coding Algorithm is a particular type of optimal prefix code that is commonly used for lossless data compression. It assigns variable-length codes to the input characters, based on the frequencies of their occurence. The most frequent character is given the smallest length code Huffman encoding requires the use of a number of different data structures together.            	| Be generally useful to compress the data in which there are frequently occurring character and useful when dealing with small sets of items, such as character strings     	| Huffman coding is not always optimal among all compression methods - it is replaced with arithmetic coding or asymmetric numeral systems if better compression ratio is required      	|
| <strike>Extended Huffman Coding</strike>                       	|             	|      	|      	|
| <strike>Adaptive Huffman Coding</strike>      K-means clustering will group similar colors together into ‘k’ clusters (say =4) of different colors (RGB values). Therefore, each cluster centroid is the representative of the color vector in RGB color space of its respective cluster	|             	|      	|      	|
| K-mean clustering                             	| K-means clustering will group similar colors together into k clusters (say k=64) of different colors (RGB values). Therefore, each cluster centroid is the representative of the color vector in RGB color space of its respective cluster            	|      	|      	|


## Resource:
----

- <strike>Colab notbook.</strike>

- <strike>Video demo.</strike>

## Information about team
----
1. Trần Đình Khang, email: trandinhkhang0279@gmail.com

2. Trần Thị Phương Thảo, <strike>email</strike>

3. Nguyễn Văn Tiến, email: tiennvuit@gmail.com .


## References:

- [Run Length Encoding](https://www.geeksforgeeks.org/run-length-encoding/)

- [Shannon-Fano-Algorithm](https://github.com/Mohammed-Ashour/Shannon-Fano-Algorithm)

- [Huffman-Coding-Algorithm](https://github.com/bhrigu123/huffman-coding)

- [K-mean clustering](https://www.geeksforgeeks.org/image-compression-using-k-means-clustering/)
