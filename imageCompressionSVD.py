'''
Final Project for 21-344 Numerical Linear Algebra (Spring 2019) @ CMU 
Instructor: Professor Jason Howell
Authors: Ben Yuan and Yirui Zhu

Code Reference: https://www.frankcleary.com/svdimage/ 
'''

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import sys
import copy
import sklearn.datasets as ds
from sklearn.decomposition import PCA

# INPUT: RGB image
# OUTPUT: grayscale image matrix of the input image
def imageToMatrix(imagename) :
    img = Image.open(imagename)
    # turn the image gray
    imggray = img.convert('LA')
    imgmat = np.array(list(imggray.getdata(band=0)), float)
    imgmat.shape = (imggray.size[1], imggray.size[0])
    matrix = np.matrix(imgmat)
    return matrix

# INPUT: 
# imagematrix: the grayscale image matrix
# k: the first k largest eigenvalues to be kept
# OUTPUT: 
# the compressed grayscale image matrix
def compress(imagematrix, k):
    U, sigma, V = np.linalg.svd(imagematrix)
    image_compressed = np.matrix(U[:, :k]) * np.diag(sigma[:k]) * np.matrix(V[:k, :])
    plt.imshow(image_compressed, cmap='gray')
    plt.show()
    return image_compressed


def main(imagename, n):
    matrix = imageToMatrix(imagename)
    compress(matrix, n)

if __name__ == '__main__':
    imagename = sys.argv[1]
    n = sys.argv[2]
    n = int(n)
    main(imagename, n)








