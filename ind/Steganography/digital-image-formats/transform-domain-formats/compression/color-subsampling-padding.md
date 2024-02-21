# Color subsampling and padding
* Human eyes less sensitive to changes in color => CrCb downsampled before DCT => higher compression ratio
1. Divide image into 16x16 pixel macroblocks
2. Each macroblock produces 4 8x8 luminance blocks, 1,2,or4 blocks for each chrominance(dependent on chrominance subsampling)
	1. If CrCb subsampled by factor of 2 in each direction, each macroblock will only have 1 8x8 Cr and Cb blocks (and ofc 4 Y blocks) => 4:1:1
	2. If neither chrominance subsampled => 4:4:4
	3. If CrCb subsampled in one direction => 4:2:2
	4. Cr 1 direction, Cb bidirection => 4:2:1, etc
3. If image dimensions MxN are not multiples of 8, image is padded to nearest larger multiples
	* $8\lceil\frac{M}{8}\rceil\times8\lceil\frac{N}{8}\rceil$
4. Before applying DCT, all pixel values are shifted by subtracting 128 from them