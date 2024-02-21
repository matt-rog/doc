# JPEG - Transform domain format
- People perceive images as segments w/ texture, NOT matrices of pixels
- We are fairly insensitive to changes in color or high-spatial-frequency #lookup 
- Matrix model **inefficient for storage** => **transform img data to other domain**
- Discrete Cosine Transform (DCT) => JPEG (compression, lossy)
- Discrete Wavelet Transform (DWT) => JPEG 2000
JPEG: Joint Photographic Experts Group

## Compression Steps
#### 1. Color transformation (opt)
- RGB => YCrCb, enables higher compression ratios w/ same fidelity
#### 2. Division into blocks + sampling
* Luminance Y signal divided into 8x8 blocks
* Chrominance signals Cr & Cb may be subsampled before dividing into blocks
#### 3. DCT Transform
* For each block, YCrCb signals transformed from **spatial domain** => **frequency domain** using DCT
* DCT, change of basis representing 8x8 matrices
#### 4. Quantization
* Resulting transform coefficients, quantized by dividing them by integer value (quantization step), rounded to nearest integer
* YCrCb may use diff. quantization tables
* Larger values of quantization steps => higher compression ratio, more distortion
* Irreversible!
#### 5. Encoding and lossless compression
* Quantized DCT coefficients are arranged in zig-zag order, encoded w/ bits, losslessly compressed (Huffman, arithmetic)

## Viewing JPEG
1. Obtain spatial-domain representation from JPEG file
	* reverse the first 5 steps above
2. JPEG bit stream parsed, decompressed, 2D array of quantized DCT coefficients formed
3. Coefficients in each block multiplied by quantization steps
4. Inverse DCT applied to produce raw pixel values
5. Values rounded to integers from dynamic range {0...255}