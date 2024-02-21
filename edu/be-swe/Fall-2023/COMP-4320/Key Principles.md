[[OSI Ref Model]]
[[TCP-IP Ref Model]]
Network: Set of **independent** (separated by hardware, vendor, OS) machines which can communicate

### Home Applications
* Metcalfe's Law - the financial value or influence of a telecommunications network is proportional to the square of the number of connected users of the system (n^2)
* RFID: Radio Frequency Identification

### Mobile Users
* Hotspots based on 802.11 standard
* SMS: Short Messaging Service
* NFC: Near Field Communication
* Sensor Networks: Nodes that gather and relay information about the physical world (car systems)

### Transmission Types
* Broadcast: 1 -> ALL
* Multicast: 1 -> Some
* Unicast: 1 -> 1 (point->point)

# Issues to Tackle
* Error detection/correction
* Routing
* Addressing, naming
* Scalability
* Flow control: regulates traffic host->host
* Congestion control: regulates traffic host->network->host
* Confidentiality/authentication

## Networking = Complex Problem -> Divide & Conquer
* Communication should be broken into layers s.t.
	* Each layer has a well-defined function
	* **Adjacent** layers have neat **interfaces**
	* Adjacent layers exchange minimal info
	* Each layer hides details from upper layers
* Peer->peer comms: protocol
	* Peers must communicate on the same level
* Adjacent layer comms: Interface
	* Above layers request service from lower (adjacent) level
* Protocol: set of rules
* Header: message exchanged from layer n->n



