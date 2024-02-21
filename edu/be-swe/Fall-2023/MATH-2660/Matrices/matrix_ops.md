# Operations w/ Matrices
### Convention to represent matrices
1. An uppercase letter
2. Representative element enclosed in numbers $[a_{ij}]$
3. A rectangular array of numbers

### Equality of matrices
* Two matrices $A=[a_{ij}]$ and $B=[b_{ij}]$ are equal iff they have the same size and $a_{ij} = b_{ij}$  for $1\leq i\leq m$ and $1\leq j\leq n$

### Def: Matrix Multiplication
Product has the rows of A and the columns of B
$$AB=[c_{ij}]$$
$$c_{ij}=\sum_{k=1}^n a_{ik}b_{kj}$$
### Linear Combinations of Column Vectors
* Matrix product Ax is the linear comb. of column vectors $a_{1}\dots a_{n}$ s.t. for coefficient matrix A,
	$$x_{1}\begin{bmatrix}a_{11}\\ \vdots \\ a_{m1}\end{bmatrix}
	\dots 
	x_{n}
	\begin{bmatrix}a_{1n}\\ \vdots \\ a_{mn}\end{bmatrix}$$
	... the system Ax=b is consistent iff b can be expressed as such a linear combination where the coefficients of the linear combination are a soln. of the system
	e.g.
	$$\begin{bmatrix}1&2\\3&4\end{bmatrix}
	\begin{bmatrix}x_{1}\\x_{2}\end{bmatrix}
=
\begin{bmatrix}x_{1}+2x_{2}\\3x_{1}+4x_{2}\end{bmatrix}
=\begin{bmatrix}x_{1}\\3x_{2}\end{bmatrix}
+
\begin{bmatrix}2x_{2}\\4x_{2}\end{bmatrix}
=
x_{1}\begin{bmatrix}1\\3\end{bmatrix}
+x_{2}\begin{bmatrix}2\\3\end{bmatrix}$$
