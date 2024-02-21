# Data Link Layer
Handles:
* Connectionless(?) layer that runs across networks, enables packet-switching networks
* Describes standards for serial lines + ethernet
* Really an interface between hosts + transmission links
* Does addressing too ig
###### Design Issues
1. Providing a well-defined service interface to the network layer
2. Deal with transmission errors
3. Regulating flow of data s.t. slow receivers are not swamped by fast senders

Data link layer takes packets from network => **frames**
Possible services to network layer
1. Unacknowledged connectionless service
	1. Source sends ind. frames to dest. machine w/o having dest. ack them
	2. Best where error rate are very low
		1. i.e. Ethernet
2. Acknowledged connectionless service
	1. Unreliable channels, WiFi
3. Unacknowledged connection-oriented service

##### MAC services LL !!