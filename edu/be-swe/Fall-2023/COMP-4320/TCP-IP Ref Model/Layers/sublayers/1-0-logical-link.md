# Logical Link (Sub)Layer
Handles addressing, framing, error+flow control

## Framing
3.1.2
#### Byte Counting
* Start each frame w/ num of bytes in the frame (including the byte count)
* One frame is corrupted, throws whole series off
#### Flag Bytes w/ Byte Stuffing
| FLAG | Header | Payload field | Trailer | Flag |
| ---- | ------ | ------------- | ------- | ---- |


| OG Bytes     | After stuffing (payload) |
| ------------ | ------------------------ |
| A-FLAG-B     | A-ESC-FLAG-B             |
| A-ESC-B      | A-ESC-ESC-B              |
| A-ESC-FLAG-B | A-ESC-ESC-ESC-FLAG-B     |
| A-ESC-ESC-B  | A-ESC-ESC-ESC-ESC-B      |
##### Bit stuffing
* Flag in binary = 0x7E = 01111110
* How to send a Flag as part of the payload field?
	* **Sender**: after every sequence of 5 1's, **insert** a 0 (ESC)
	* **Receiver**: after every sequence of 5 1's, **remove** the 0 (is there is one)

## Error control
3.1.3,3.2
* Detects error transmission
* May correct error transmissions
* Physical layer cannot guarantee an ideal channel (no corruption)
* Essentially adding **check bits** to detect and possibly correct
### Error detection
#### Parity
* Sender adds a parity bit to the words s.t. the total number of bits (including parity) bit is even (**Even parity**)
	* 01011 **1** =medium=> 000011
		* If even number of bits are flipped, the numbers of 1's remain the same
#### Cyclic Redundancy Code
#### Checksum
### Error correction
#### Crossed Parity
#### Hamming Code
* Can detect distance-1 corrupted bits
* Can detect & correct floor((n-1)/2) corrupted bits

## Flow control
3.1.4
Feedback-based flow control
- Receiver sends back info to sender, asking for more data
Rate-based flow control
* Protocol's built-in mechanism limits rate at which the sender may transmit data, w/o feedback from receiver