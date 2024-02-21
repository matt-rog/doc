# Rank of a Matrix and Systems of Linear Equations

Row  space: subspace of R^n spanned by the row vectors of A
### Basis for Row Space of Matrices
If A is row-equivalent to B in row-echelon form, then the  nonzero row vectors of B form a basis for the row space of A
1. (If necessary) convert row vectors into some matrix
2. REF this matrix (as best you can)
3. Take non-zero row-vectors => that is your basis
### Basis for Column Space of Matrices
1. Transpose A
2. REF this matrix (as best you can)
3. Take non-zero row-vectors => your basis
## Rank
rank of some matrix A
- rank(A) = dim of row space || dim of column space
- aka the number of nonzero rows/cols in basis

## Nullspace of a Matrix
- Set of all solutions of homogeneous system of linear equation Ax=0 is a subspace of R^n called the nullspace of A : N(A)
- $N(A)=\lbrace x \in R^{n}: Ax=0 \rbrace$
- dimension of nullspace of A => **nullity** of A

1. Append 0 column to matrix
2. REF matrix
3. Find solution set to matrix s.t. =0
4. Take solutions => their own column vector