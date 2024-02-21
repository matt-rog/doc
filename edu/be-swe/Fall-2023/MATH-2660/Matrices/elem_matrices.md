# Elementary Matrices
## Def: Elementary Matrix
An nxn matrix that can be obtained from $I_{n}$ by a single row op.

# Type 1: Row-switching Transformations
$T_{ij}$ is made by swapping rows i and j of I
$$T_{23}=\begin{bmatrix}
1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1
\end{bmatrix}$$
$T_{ij}A$ results in swapping rows i and j of A
#### Properties
1. Inverse: $T_{ij}^{-1} = T_{ij}$ (itself)
2. $\det(T_{ij})=-1$
3. $\det(T_{ij}A)=-\\det(A)$

# Type 2: Row-multiplying Transformations
Multiplies all elements on $R_{i}$ by m (m>0)
$D_{i}(m)$ is made by replacing the 1 with m on the ith row of I
$$D_{2}(4)=\begin{bmatrix}
1&0&0&0\\0&4&0&0\\0&0&1&0\\0&0&0&1
\end{bmatrix}$$
$D_{i}(m)A$ results in multiplying m to $R_{i}$ of A
#### Properties
1. Inverse: $D_{i}(m)^{-1} = D_{1}\left( \frac{1}{m} \right)$
2. $\det(D_{i}(m))=m$
3. $\det(D_{i}(m)A)=m\det(A)$

# Type 3: Row-addition Transformations
Adds row j multiplies by scalar m to row i
$L_{ij}(m)$ is made by putting an m at $I_{ij}$
$$L_{31}(6)=\begin{bmatrix}
1&0&0&0\\0&1&0&0\\6&0&1&0\\0&0&0&1
\end{bmatrix}$$
$L_{ij}(m)A$ results in $R_{i}+mR_{j}$ in A
#### Properties
1. Inverse: $L_{ij}(m)^{-1} = L_{ij}(-m)$
2. $\det(L_{ij}(m))=1$
3. $\det(L_{ij}(m)A)=\det(A)$