# The main program
import numpy as np
from config import algorithms
from utils import get_arguments



def main(args):
    try:
        algorithm = algorithms[args['algorithm']]
    except:
        print("The algorithm is not valid")
        exit(1)


if __name__ == '__main__':
    args = get_arguments()
    main(args)
