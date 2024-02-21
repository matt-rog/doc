# Internet/Network Layer
(Basically just [[Network]] but more functionality)
* Internet is a store-and-forward packet switching system
* Permits hosts to inject packets into any network and have them travel independently to destination
* Higher layers fix packet disorder
* Defines:
	* Packet/format protocol: IP (internet protocol)
	* Companion protocol: ICMP (internet control message protocol)
* Delivers IP packets where they need to go

#### Connectionless
- Each message is sent as independent entity (NO STATE INFO kept on hosts, routers, l3 switches)
- Datagrams carry messages
- Items of same conversation may take different paths
#### Connection Oriented
- Virtual circuit over which all messages will transit
- Intermediary nodes keep state about circuit

### Routing Policy Algorithms

## Subnets
Subnet: uses subset of addressing space of its supernet
- Auburn is network with netid 131.204.0.0 (class B)
Why subnetting?
- Class A/B has large number of hosts (16M/65K)
- Hosts on same network will share a broadcast medium (65k too many for 1 medium)
How?
- Subnet mask
	Class B `10 [14-bit netid] [16-bit hostid]`
		Divide 16 bit addressing space
		hostid: `[m-bit netid] [(32-16-m)-bit hostid`
		e.g. Auburn subnet `131.204.0.0`
			hostid: `[5-bit netid][11-bit hostid]`
- Problem: How to know # m of bits of subnet ID?
	- In ex., subnetID has 16+5bits = 21 bits
- Answer:
	- use a **subnet mask** starting with 21 bits and finishing with 11 zeros
	- `1111 1111 1111 1111 1111 1000 0000 0000`
	- Subnet ID = IP addr (bitwise AND) subnet mask
- Example:
	- IP: `131.204.65.35`, subnet mask: `255.255.255.240`
		- subnetID: `131.204.65.32`
: If subnetID's are equal, they are on the same network
###### Shorthand Subnet Mask Notation
- IP `131.204.65.34` w/ subnet mask `255.255.255.0` => `131.204.65.34/24`
- 24 = # of 1's
###### Device-Connecting Machines
- If two machines have different subnet IDs, there **IS** a router (L3 switch) between the machines

## IP Routing
###### Router IP Mechanics
```java
if(IP of machine = IP destination){
	// Hand packet to appropriate transport layer protocol (using protocol field)
} else {
	if(IP destination is local to me){
		// Get MAC of IP destination (ARP)
		// Ask data link to send packet to MAC dest.
	} else {
		// Read routing table to find next router
		// Get MAC of router
		// data link -> packet -> MAC dest. rtr.
	}
}
```
- Using longest IP match as heuristic
	- else, default entry

## IP Helpers
#### ARP (Address Resolution Protocol)
RFC: 826
In: IP address -> Out: MAC address
Scenario: ARP receives IP address resolution request:
1. Search cache for IP (ARP table)
2. If entry, return MAC
3. Else:
	1. Broadcast local net (Who has IP addr?)
	2. Wait...
	3. Store result in cache, return MAC
### DHCP (Dynamic Host Configuration Protocol)
- Every machine needs following info to communicate over internet
	- IP addr
	- Subnet mask
	- IP addr of DNS (maps names => ip addr)
	- IP addr of default gateway (router to go to internet)
Can achieve this through config file or DHCP
- Every machine should have reachable DHCP dever
- DHCP client on machine will
	- discover DHCP server
	- collect necessary details ^
### ICMP (Internet Control Message Protocol)
- Helps w/ anomalies such as
	- TTL reaches 0, packet must be dropped
	- Routing error
	- An IP must be fragmented, but its fragmentation flag forbids it
- On anomalous event:
	- build ICMP message containing beginning of faulty packet, including IP header + transport layer header
	- Sends message to source of faulty packet