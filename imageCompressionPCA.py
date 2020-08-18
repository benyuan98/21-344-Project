'''
Final Project for 21-344 Numerical Linear Algebra (Spring 2019) @ CMU 
Instructor: Professor Jason Howell
Authors: Ben Yuan and Yirui Zhu

Code Reference: https://blog.csdn.net/u012162613/article/details/42177327 
'''

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as ds
from sklearn.decomposition import PCA
from imageCompressionSVD import imageToMatrix


# INPUT: matrix
# OUTPUT: each column of the input matrix has a mean of zero
def zeroMean(dataMat):     
    # compute mean by columns
    meanVal = np.mean(dataMat,axis=0)     
    newData = dataMat - meanVal
    return newData

# INPUT: 
# eigVals: eigenvalues of a matrix
# percentage: the desired proportion of explained variance 
# OUTPUT:
# the minimum k to meet the desired proportion of explained 
# variance along the first k eigenvectors
def percentage2n(eigVals,percentage):
    # sort eigenvalues in ascending orders
    sortArray = np.sort(eigVals)   
    # reverse to sort eigenvalues in descendign orders
    sortArray = sortArray[-1::-1]  
    arraySum = sum(sortArray)
    tmpSum = 0
    num = 0
    for i in sortArray:
        tmpSum += i
        num += 1
        if (tmpSum >= arraySum*percentage):
            return num

# INPUT:
# matrix: grayscale image matrix
# percentage: the desired proportion of explained variance
# OUTPUT:
# the minimum k to meet the desired proportion of explained 
# variance along the first k eigenvectors
def pca(matrix, percentage):
    newMatrix = zeroMean(matrix)
    # compute the covariance matrix
    covMat = np.cov(newMatrix, rowvar = 0)    
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))
    n = percentage2n(eigVals,percentage)
    return n

# Draws the following curves in one plot:
# 1. Explained Variance Ratio of the n-th Principal Component vs n-th Principal Components
# 2. Cumulative Explained Variance Ratio vs n-th Principal Components
# 3. A vertical line that indicates where the input percentage and n are on the x-axis
def variance_n(matrix, percentage, n):   
    data = matrix
    pca_trafo = PCA().fit(data)

    plt.semilogy(pca_trafo.explained_variance_ratio_, 'o', markersize=1,
                 label = "exlained variance ratio of the n-th principal component")

    plt.semilogy(pca_trafo.explained_variance_ratio_.cumsum(), 'o', markersize=1,
                 label = "cumulative explained variance ratio");

    plt.xlabel('n-th principal components', fontsize=12)
    plt.ylabel('explained variance ratio', fontsize=12)
    plt.axvline(x=n, linestyle = "--", color = "red", label = str(100*percentage) + "% " + "cumulative explained variance at n = " + str(n))
    plt.legend(loc="lower left")
    plt.show()

def main(imagename, percentage):
    matrix = imageToMatrix(imagename)
    n = pca(matrix, percentage)
    print(n)
    variance_n(matrix, percentage, n)

if __name__ == '__main__':
    imagename = sys.argv[1]
    percentage = sys.argv[2]
    percentage = float(percentage)
    main(imagename, percentage)