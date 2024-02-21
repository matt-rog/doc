# Affine Cipher
## Theory
* Alternative implementation of substitution, however it restricts encryption functions to the form $$e(x)=(ax+b)\bmod{26}$$
	* $a,b\in\mathbb{Z}_{26}$. These functions are called **affine** functions
		* When a=1, it's just a **shift** cipher
In order for decryption, the affine function needs to be injective (1:1)

For any $y\in\mathbb{Z}_{26}$, we need this congruence to have a unique solution for x.
$$ax+b \equiv y\bmod{26} \Longleftrightarrow ax \equiv y-b\bmod{26}$$
y-b varies with y, so let's study $ax \equiv y-b\bmod{26}$
* This has a unique soln. iff $\gcd{(a,26)}=1$, gcd = greatest common divisor
* $\gcd{(a,26)}>1$ => 2 or more distinct solutions, not injective, **invalid encryption func**
	* At least 2 distinct solutions: x=0, x=26/d

If $\gcd{(a,26)}=1$, for some $x_1,x_2$
$$ax_1 \equiv ax_2\bmod{26}$$
$$a(x_1-x_2)\equiv0\bmod{26}$$
$$26\mid a(x_1-x_2)$$
If $\gcd{(a,b)}=1\text{ and }a\mid bc$, then $a \mid c$ 
$$26\mid (x_1-x_2) \Longleftrightarrow x_1 \equiv x_2\bmod{26}$$


#### Finding number of distinct solutions
Recap, if $\gcd{(a,26)}=1$, then num of solns in $\mathbb{Z}_{26} \leq 1$ for $ax\equiv y\bmod{26}$. Let x vary over $Z_{26}$, axmod(26) takes on exactly 26 distinct values modulo 26. Thus, for any $y\in\mathbb{Z}_{26}, ax\equiv y\bmod26$ has a unique solution for x. *26 is arbitrary*
> THM. The congruence $ax \equiv b\bmod m$ has a unique solution $x \in \mathbb{Z}_{m}$ for every $b \in \mathbb{Z}_{m}$ iff $\gcd{(a,m)}=1$.

e.g. Since 26=2x13, the values of $a\in \mathbb{Z}_{26}$ s.t. $\gcd{(a,26)}=1$, are 
	a=1,3,5,7,9,11,15,17,19,21,23,25 | 12 values
 * b can be any element in $\mathbb{Z}_{26}$
 => The Affine cipher has 12x26=312 possible keys. (too small to be secure)
##### Generalizing distinct num of solns
Let modulus = m
> DEFN: Prime
> 	An integer p>1 is prime if it has no positive divisors other then 1 and p. Every integer m>1 can be factored as a product of powers in a unique way. $60=2^2\times3\times5$
> DEFN: Relatively prime
> 	Suppose $a \geq 1$ and $m \geq 2$ are integers. If $\gcd{(a,m)}=1$, a and m are relatively prime. The number of integers in $\mathbb{Z}_{m}$ that are relatively prime to m is denoted by $\phi{(m)}$ (Euler-phi function)

We can give the value of $\phi(m)$ in terms of the prime power factorization of m.
> THM
> 	Suppose $$m=\prod_{i=1}^{n}p_i^{e_{i}}$$
> 	where the $p_i$'s are distinct primes and $e_i>0,1\leq i \leq n$. Then$$\phi(m)=\prod_{i=1}^{n}(p_i^{e_{i}}-p_i^{e_{i}-1})$$

Number of keys in Affine Cipher over $Z_{m}$ is $m\phi(m)$, where $\phi(m)$ is given by above.
Number of choices for b is m, and the number of choices for a is $\phi({m})$, where encryption function is $e(x)=ax+b$. 
e.g. $m=60,\phi(m)=(2^2-2)(3-1)(5-1)=2\times2\times4=16$ => # of keys = 960
#### Decryption
To decrypt, solve $y\equiv ax+b(\bmod 26)$ for x. Need multiplicative inverse
>DEFN: Multiplicative Inverse
>	Suppose $a\in \mathbb{Z}_m$, the multiplicative inverse of $a\bmod m$, denoted $a^{-1}\bmod m$, is an element in $a'\in \mathbb{Z}_m$ s.t. $aa'\equiv a'a \equiv 1\bmod m$. If m is fixed, write $a^{-1}$ for $a^{-1}\bmod m$.

a has multiplicative inverse modulo m iff $\gcd(a,m)=1$, if a multiplicative inverse exists, it is unique modulo m. $$b=a^{-1} \Longleftrightarrow a=b^{-1}$$
If p is prime, then every non-zero element of $Z_p$ has a multiplicative inverse. A ring in which this is true is called a field.
$$y\equiv ax+b(\bmod26) \Longleftrightarrow ax \equiv y-b(\bmod26)$$
$\gcd(a,26)=1$, a has multiplicative inverse modulo 26. Multiply both sides by a^-1$$a^{-1}(ax) \equiv a^{-1}(y-b)(\bmod26)$$ $$a^{-1}(ax) \equiv (a^{-1}a)x \equiv 1x \equiv x(\bmod26)$$
$$d(y)=a^{-1}(y-b)\bmod26$$

## Cryptosystem
> Affine Cipher
> 	Let $\mathbb{P}=\mathbb{C}=\mathbb{Z}_{26}$ and let $$\mathbb{K}=\set{(a,b)\in\mathbb{Z}_{26}\times\mathbb{Z}_{26}:\gcd(a,26)=1}$$
> 	For $K=(a,b)\in\mathbb{K}$, define$$e_K(x)=(ax+b)\bmod26$$ $$
d_K(y)=a^{-1}(y-b)\bmod26
$$ $(x,y\in\mathbb{Z}_{26})$

e.g. K=(7,3). 7^-1 mod 26 = 15.
$$\begin{aligned}
&e_K(x)=7x+3 \\
&d_K(x)=15(y-3)=15y-19
\end{aligned}$$
#### Encryption
P: `hot` x = h:7, o:14, t:19,  (derived from letters modulo 26)
$$\begin{aligned}
& h:(7\times7+3)\bmod 26=0 \\
& o:(7\times14+3)\bmod 26=23 \\
& t:(7\times19+3)\bmod 26=6 \\
\end{aligned}$$
#### Decryption
C: `AXG` x = A:0, X:23, G:6
$$\begin{aligned}
& A:(15\times0-19)\bmod 26=7 \\
& X:(15\times23-19)\bmod 26=14 \\
& G:(15\times6-19)\bmod 26=19 \\
\end{aligned}$$
7,14,19 => `hot` :)