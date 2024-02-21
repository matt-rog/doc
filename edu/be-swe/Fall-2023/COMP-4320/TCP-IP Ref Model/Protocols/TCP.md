# Transmission Control Protocol
RFC: 793
Protocol #17
- Connection-oriented, allows byte streams to be delivered w/o error
- Segments incoming byte stream into discrete messages -> [[2-internet]]

- Data exchange is bidirectional (both endpoints send)
Handles 3 functions
1. Error detection + recovery
	2. (ip is only best effort, can reorder, corrupt, etcs)
2. Flow control
3. Congestion control

What can happen to segment?
- Reach dest. unaltered
- reach dest. corrupted

Dealing w/ corrupted segments
- Use checksum covers TCP header and payload. Add all bits and sm sm
- Recover corrupted segment by resending segment

Dealing w/ out of order segments
