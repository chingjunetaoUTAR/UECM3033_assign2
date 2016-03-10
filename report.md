UECM3033 Assignment #2 Report
========================================================

- Prepared by: Ching June Tao
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/chingjunetaoUTAR/UECM3033_assign2](https://github.com/chingjunetaoUTAR/UECM3033_assign2)

Explain your selection criteria here.

I will the is matrix A positive definite or not. If matrix A is positive definite, SOR method will be used to solve the system. If matrix A is not positive is not positive definite, LU decomposition will be used to solve the system. This is because when the matrix is not positive definite, we could not find an optimum ω for SOR method and it will not converge to the solution.
I use eigen values of matrix A and symmetricity of matrix A to check is it positive definite. 

Explain how you implement your `task1.py` here.

In LU decomposition, I use scipy.linalg.lu(A) to decompose matrix A to P, L and U.
P is Permutation matrix.
L is Lower Triangular matrix.
U is Upper Triangular matrix.

Permutation matrix is used in case the pivot element of first row of matrix A is not the largest, the algorithm might get error when solving the system. 

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Lenna.png)

![Lenna.png](Lenna.png)

How many non zero element in $\Sigma$?

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?


-----------------------------------

<sup>last modified: change your date here</sup>
