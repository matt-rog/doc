# Shift Cipher
## Theory
Shift cipher is dependent on modular arithmetic

## Cryptosystem
> Shift Cipher
> 	Let $\mathbb{P}=\mathbb{C}=\mathbb{K}=\mathbb{Z}_{26}$ for $0\leq\mathbb{K}\leq25$, define $$e_{K}(x)=(x+K)\bmod26$$
> 	and	$$d_{K}(y)=(y-K)\bmod26$$
$(x,y\in\mathbb{Z}_{26})$
- K=3, => Caesar cipher

##### Example
1. $\mathbb{P}=$ `wewillmeetatmidnight`
2. Find each the corresponding index of each letter in the alphabet (x)
3. `22,4,22,8,11,11,12,4,4,19,0,19,12,8,3,13,8,6,7,19`
4. Add 11 to each value, then reduce each value modulo 26
5. `7,15,7,19,22,22,23,15,15,4,11,4,23,19,14,24,19,17,18,4`
6. $\mathbb{C}=$ `HPHTWWXPPELEXTOYRSE`