# Discrete Cosine Transform
For 8x8 block of luminance/chrominance values $B[i,j], i,j =0,...,7$, the 8x8 block of DCT coefficients $d[k,l], k, l=0,...,7$ is computed as a linear combination of luminance values,
$$
d[k,l]
=\sum_{i,j=0}^{7}f[i,j;k,l]B[i,j]
=\sum_{i,j=0}^{7}\frac{w[k]w[l]}{4}
   cos\frac{\pi}{16}k(2i+1)
   cos\frac{\pi}{16}l(2j+1)
   B[i,j]
$$
* $f[i,j;k,l]=(\frac{w[k]w[l]}{4})cos\frac{\pi}{16}k(2i+1)cos\frac{\pi}{16}l(2j+1)$
* $w[0] = \frac{1}{\sqrt{2}}, w[k>0]=1$
* Coefficient $d[0,0]$ is called the DC coefficient, DC term
* Remaining coefficients with $k+l>0$ = AC coefficients

**Inverse DCT**
$$
B[i,j]
=\sum_{i,j=0}^{7}\frac{w[k]w[l]}{4}
   cos\frac{\pi}{16}k(2i+1)
   cos\frac{\pi}{16}l(2j+1)
   d[k,l]
$$

DCT can be interpreted as change of basses in the vector space of all 8x8 matrices, where sum of matrices and multiplication by a scalar are defined in the elementwise manner and the dot product betweeen matrices X and Y is
$$X\timesY=\sum_{i,j=0}^{7}X[i,j]Y[i,j]$$
For fixed pair, (k,l) call 8x8 matrix f[i,j;k,l] the (k,l)th based pattern
All 64 patterns form an orthonormal system
$$\sum_{i,j=0}^{7}f[i,j;k,l]f[i,j;k',l']=\delta(k-k')\delta(l-l')$$ for all $k,k',l,l'\in\{0,...,7\}$
* where $\delta$ is the Kronecker delta, $$\delta(x)=\begin{cases}1 \text{when }x=0\\0\text{when }x\neq0\end{cases}$$