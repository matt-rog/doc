# Gaussian Elim & Gauss-Jordan Elim
## Def: Matrix
If *m* and *n* are positive integers, then an $m*n$ matrix is the rectangular array:
	$$A_{m,n}\begin{bmatrix} a_{11} & a_{12} & ... &a_{1n} \\ a_{21} & a_{22} & ... &a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & ... &a_{mn}\end{bmatrix}$$
### Elementary Row Operations
Same as SLE
1. Interchange 2 rows
2. Multiple row by nonzero constant
3. Add multiple of row to another row
*Map SLE -> row, var+ouput -> col*

---
# Gaussian Elim
### REF
A matrix is in REF iff:
1. All-zero rows are at the bottom
2. For non-all-zero rows, the first nonzero entry is 1 (the leading 1)
3. For 2 successive non-all-zero rows, the leading 1 in the higher row is farther to the *left* than the leading 1 in the higher row
eg. Use elem row ops to rewrite the matrix in REF.
	Solve the sys $$\begin{cases}x-2y+3z=9\\-x+3y=-4\\2x-5y+5z=17\end{cases}$$
	Sol: $$
	\begin{bmatrix}1&-2&3&9\\-1&3&0&-4\\2&-5&5&17\end{bmatrix}
	\to{R_2+R_1}\to
	\begin{bmatrix}1&-2&3&9\\0&1&3&5\\2&-5&5&17\end{bmatrix}
	\to{R_{3}-2R_{1}}\to{meh_{idc^{to_{work^{on_{this}}}}}}
	$$
# Gauss-Jordan Elim
### Reduced REF
A matrix is in RREF when every column with a leading 1 has all zeros in its position above and below it

---
