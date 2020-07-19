import numpy as np


def predictorP1(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = A
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i][j-1]
    return prediction_matrix


def predictorP2(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = B
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i-1][j]
    return prediction_matrix

def predictorP3(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = C
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0 or j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i-1][j-1]
    return prediction_matrix


def predictorP4(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = A + B - C
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0 or j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i][j-1] + image[i-1][j] - image[i-1][j-1]
    return prediction_matrix


def predictorP5(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = A + (B-C)/2
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0 or j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i][j-1] + (image[i-1][j] - image[i-1][j-1])/2
    return prediction_matrix


def predictorP6(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = B + (A-C)/2
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0 or j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = image[i-1][j] + (image[i][j-1] - image[i-1][j-1])/2
    return prediction_matrix

def predictorP7(image: np.ndarray):
    """
    ...........
    ....C B....
    ....A X....
    ...........
    Predict the value of X by formula: X = A + B / 2
    """
    prediction_matrix = np.zeros(image.shape)

    rows = image.shape[0]
    cols = image.shape[1]

    for i in range(rows):
        for j in range(cols):
            # Ignore the first column
            if i == 0 or j == 0:
                prediction_matrix[i][j] = image[i][j]
            else:
                prediction_matrix[i][j] = (image[i-1][j] + image[i][j-1])/2
    return prediction_matrix


predictors = {
    'P1': predictorP1,
    'P2': predictorP2,
    'P3': predictorP3,
    'P4': predictorP4,
    'P5': predictorP5,
    'P6': predictorP6,
    'P7': predictorP7,
}
