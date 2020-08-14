import argparse
import os
import time
import numpy as np
import cv2
from sklearn.cluster import KMeans
import pickle
from .base import Base

class Kmean(Base):
    def __init__(self):
        self.name = "K mean clustering for image compression"

    def calculate_compression_ratio(self, input:str, clusters):
        input_image = input
        print("[INFO] Calculate the needed bits...")
        rows = input_image.shape[0]
        cols = input_image.shape[1]
        origin_bits = rows*cols*3*8
        encoded_bits = int(rows*cols*3*np.ceil(np.log2(clusters)))
        ratio = 8 / np.ceil(np.log2(clusters))

        print("- The number of bits needed represent image is {}".format(origin_bits))
        print("- The number of bits needed represent the ENCODED image: {}".format(encoded_bits))

        return ratio

    def compress(self, input: np.ndarray, clusters: int):

        image = input
        print("[INFO] Preprocressing ...")
        # Get dimension of the original image
        rows = image.shape[0]
        cols = image.shape[1]

        #Flatten the image
        reshaped_image = image.reshape(rows*cols, 3)

        print("[INFO] Compressing ...")
        #Implement k-means clustering to form clusters
        kmeans = KMeans(n_clusters=clusters)
        kmeans.fit(reshaped_image)

        return (image.shape, kmeans.cluster_centers_, kmeans.labels_)


    def decompress(self, image_shape: tuple, cluster_centers:np.ndarray, labels: np.ndarray):
        print("[INFO] Decompressing ...")
        # Replace each pixel value with its nearby centroid
        decompressed_image = cluster_centers[labels]
        decompressed_image = np.clip(decompressed_image.astype('uint8'), 0, 255)

        #Reshape the image to original dimension
        decompressed_image = decompressed_image.reshape(image_shape)
        return decompressed_image


def get_arguments():
    parser = argparse.ArgumentParser(description='The K-mean clustering algorithm for image compression')
    parser.add_argument('--mode', '-m', default='compress',
                        choices=['compress', 'decompress'],
                        help='The mode for the algorithm work')
    parser.add_argument('--input', '-i', default='./input/input_kmean.jpg',
                        help='The input file path')
    parser.add_argument('--output', '-o', default='./output/output_kmean.pl',
                        help='The output file path')
    parser.add_argument('--clusters', '-k', default=8, choices=[4, 8, 16, 32, 64, 128],
                        type=int, help='The number of clusters')
    return vars(parser.parse_args())


def main(args):

    if args['mode'] == 'compress':
        # Read the image data from disk
        try:
            img = cv2.imread(os.path.abspath(args['input']))
        except:
            print("The image is not found")
            exit(0)

        print("[INFO] The origin image...")
        cv2.imshow('Origin image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        kmean = KMean()
        # Run the compression algorithm
        (shape, cluster_centers, labels) = kmeam.compress(image=img, clusters=args['clusters'])

        compress_ratio = kmean.calculate_compression_ratio(input=img, clusters=args['clusters'])
        print("[INFO] The compression ratio is {}".format(compress_ratio))
        # Store the output data to disk
        with open(args['output'], 'wb') as f:
            pickle.dump((shape, cluster_centers, labels), f)

    elif args['mode'] == 'decompression':
        # Check the input file whether or not exis
        print(args['input'])
        if not os.path.isfile(args['input']):
            print("The input file is not exis")
            exit(1)

        # Read compressed data with pickle format
        with open(args['input'], 'rb') as f:
            shape, cluster_centers, labels  = pickle.load(f)
            decompressed_image = kmean.decompress(image_shape=shape,cluster_centers=cluster_centers, labels=labels)
            print("[INFO] Display decompressed image...")
            cv2.imshow('The compressed image with {} clusters'.format(len(cluster_centers)), decompressed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("The selected mode is not valid")
        exit(0)



if __name__ == '__main__':
    args = get_arguments()
    main(args)
