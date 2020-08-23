# Image Compression Using SVD and PCA

This is our final project for 21-344 Numerical Linear Algebra (Spring 2019) at Carnegie Mellon University. In this project, we applied Singular Value Decomposition (SVD) to image compression. We also explored how Principal Component Analysis (PCA) can be used to determine the parameter used in SVD. We found that using SVD and PCA together could compress an image effectively. For details, please see ```21-344paper.pdf``` and ```21-344presentation.pdf``` in this repository.

## How to Run These Code?

**1.** Select an image (in png format), place it in the same directory as the code and name it, e.g., ```photo.png```. 

**2.** To determine how many terms to be kept in SVD, first run ```imageCompressionPCA.py```  by the following command in Terminal:
```
python imageComrpessionPCA.py photo.png percentage
```

where ```percentage``` is the proportion of explained variance along the first k eigenvectors (cumulative explained variance).

For example, if one wants to preserve 99% cumulative explained variance of the image, run the following command in Terminal:
```
python imageComrpessionPCA.py photo.png 0.99
```

In Terminal a number ```k``` is printed.

**3.** Run the following command in Terminal to compress the image:
```
python imageComrpessionSVD.py photo.png k
```

For example, if the number ```k``` printed in step 2 is 93, run the following command in Terminal:
```
python imageComrpessionSVD.py photo.png 93
```
