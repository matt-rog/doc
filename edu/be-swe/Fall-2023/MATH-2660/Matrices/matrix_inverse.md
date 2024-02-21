# Inverse of a Matrix
## Def: Matrix Inverse
An nxn matrix is invertible (nonsingular) where there exists an nxn B s.t.
	$AB = BA = I_{n}$
	B is the *multiplicative inverse* of A. Matrices w/o inverse are singular/noninvertible
### Thm: Uniqueness of Inverse Matrix
If A is an invertible matrix, then its inverse is unique.

### Finding the Inverse of a matrix via GJE
Let A be an nxn matrix
1. Write a nx2n matrix that consists of A on the left and I on the right
	$\begin{bmatrix}A & I\end{bmatrix}$
2. If possible, reduce A to I using elementary row ops. The result will be
	$\begin{bmatrix}I & A^{-1}\end{bmatrix}$
    If not, A is noninvertible

## Properties of Invertible Matrices
Let A be invertible, k a positive integer, and c a nonzero scalar
* $A^{-1},A^{k},cA, A^T$ are invertible also, and
1. $(A^{-1})^{-1}=A$
2. $(A^k)^-1=A^{-1}A^{-1}\dots A^{-1} = ()A^{-1})^k$
3. $(cA)^{-1}=\frac{1}{c}A^{-1}$
4. $(A^T)^{-1} = (A^{-1})^T$
**Inverse of a Product**
$(AB)^{-1}=B^{-1}A^{-1}$
**Cancellation**
1. If $AC=BC\to A=B$
2. If $CA=CB\to A=B$

### Thm: SLE w/ Unique Solutions
If A is nonsingular, then the system of linear equations Ax=b has a unique solution $x=A^{-1}b$
$$\begin{cases}2x+3y+z=-1\\3x+3y+z=1\\2x+4y+z=-2\end{cases}
\Longrightarrow
\begin{bmatrix}x\\y\\z\end{bmatrix}
=
\begin{bmatrix}2&3&1\\2&3&1\\2&4&1\end{bmatrix}^{-1}
\begin{bmatrix}-1\\1\\2\end{bmatrix}$$