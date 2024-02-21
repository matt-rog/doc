comp 4300 11/28

thread - executing piece of code that shares memoery space w/ oher threates
	- group of threads cooperate
	- (piece of code, program counter, access to shared memory space
	- lightweight process
	- context switch

cuda code (parallel prog lang)
v
parallelizing compiler
v
----- GPU -----
v
threat block scheduler
vvvv
streaming multiprocessor n
vvvv
thread n
vvvv
simd instr
v
simd instr
v
etc


C code
```c
# FUNC
void daxpy(int n, double a, double *x, double *y)
{
	for(int i = 0; i<n; i++){
		y[i]=a*x[i]+y[i];
	}
}
# FUNC CALL
double w[100], z[100];
daxpy(100, 2.7, w, z);
```
CUDA code
```c
__host__ // will run on cpu

int = (n+255)/256 // how many blocks of threads are there? => 256
daxpy<<nblocks, 256>>(n, 2.7, w, z)

__global__ // parallelizable, will run on gpu
// whenever running on gpu, 3 values are already declared => no need to declare in global
// - blockIndx: which block is running
// - threadIndx: which thread within block
// - blockDim: how many threads per block
void daxpy(int n, double a, double *x, double *y){
	// need to calc i
	int i = blockIdx * blockDim + threadIdx
	if( i<n ){
		y[i]=a*x[i]+y[i];
	}
}
```

### Cache coherence
Defn
1. Read by processor P of shared location x, w/ no writes by any other processor, gets the last value written by P
2. Read by P2 of x that follows a write by P1, gets the value written by P1 if:
	1. read and write are sufficiently separated in time
	2. no other intervening writes
3. writes to the same location are **serialized** in the same order to all processors (some universally understood order of processes)

**2 Ways to guarantee coherence**
1. Write-invalidate: when a processor writes to a location in its cache, all other processors with that block in cache, invalidate their block cache. Implementation 
	1. Snooping: all processors monitor (snoop) the shared bus and invalidate blocks in their cache when the processor writes to that block. 
	2. Directory-based: There's a central directory that (may be distributed) that keeps track of which processors have each block in their caches
2. Write-broadcast-update; all processors caches when a write happens

# HW2
1.
	a. 32k/64b = 2^15/2^6=2^9 => 512b locks
	b. 64 b = 2^6 =>
	c
	d. 512 blocks + **2**way => 512/**2** => 256 sets
		256 = 2^8 => 8bit index
		20-8-6=6bits tag
	e. full assoc => 0bit index
		20-6 = 14bit tag
2.
35% load store apply => 100/135 = .79 of mem access are instr
35/135 = .26 are data

instr avg = 1+.02x100 = 3cycles
data laad store = 1 + 1 + 0.03x100 = 5 cycles

overall avg

.74x3 .26x5 => uhhh


# Final
(cum. 1/3 pre-midterm, 2/3 post-midterm)
1. Amdal's law
AMD => speedup = 1/((1-f)+f/s)
1.5 = 


11.
grab bits 8-13 (indecices) => put them in sets, overwriting when sets get full

0x5fff03e2 => set 000011