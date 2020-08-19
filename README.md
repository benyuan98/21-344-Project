# Image Compression Using SVD and PCA

This is our final project for 21-344 Numerical Linear Algebra (Spring 2019) at CMU. In this project, we applied Singular Value Decomposition (SVD) to image compression. We also explored how Principal Component Analysis (PCA) can be used to determine the parameter used in SVD. We find that using SVD and PCA together could compress an image effectively. For details, please see ```21-344paper.pdf``` and ```21-344presentation.pdf``` in this repository.

## How to Run These Code?

**1.** Put the image (in png format) you would like to compress in the same directory as the code. Let's say you named your image ```photo.png```. 

**2.** To determine how many terms to be kept in SVD, you first need to run ```imageCompressionPCA.py```  by typing the following command in the terminal:
```
python imageComrpessionPCA.py photo.png percentage
```

where ```percentage``` is the proportion of explained variance along the first k eigenvectors (cumulative explained variance).

For example, if you want to preserve 99% cumulative explained variance of the image, type the following command in the terminal:
```
python imageComrpessionPCA.py photo.png 0.99
```

In the terminal a number ```k``` is printed.

**3.** Type the following command in the terminal to compress your image:
```
python imageComrpessionSVD.py photo.png k
```

For example, if the number ```k``` printed in step 2 is 93, type the following command in the terminal:
```
python imageComrpessionSVD.py photo.png 93
```
