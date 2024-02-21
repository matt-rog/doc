# Medium Access Control (Sub)layer


### Topologies
##### Point-point channel
- Full duplex channels allow **simultaneous** communication in **both** directions
	- MAC not necessary, each user has a dedicated channel not shared w/ other (2-ay street)
- Half duplex - **alternate** communication in both directions
	- MAC necessary
##### Broadcast
(ie random access, multiaccess)
- 1 station transmit, every other station on channel hears and understands
- 2+ transmit, every station on channel hears, does not understand
	- MAC necessary (people in same room)
#### Result from Queueing Theory
- One powerful server for all is better than one weak server for each one
- Competing stations (contention based, collisions)
	- Good avg delivery time
	- No guaranteed delivery
- Collision-free
	- Higher avg delivery time
	- Guaranteed delivery time! (bounded waiting time)
### Contention | Pure Aloha
- A station emits whenever it has smth to send
- If other stations emit during any other transmission, collision!
- If collision occurs, frames must be reset
- Best possible efficiency at high load 18%
### Contention | Slotted Aloha
- Requires synchronization & division of time into discrete slots
- Slot time = time to send 1 frame
- Station emits whenever it has something to send & must wait for beginning of slot
- High load efficiency 37%
### Contention | CSMA
Carrier Sense Multiple Access
- Station listens to channel before sending
- When channel free, send
- Collisions still possible
- On collision, drop all dmgd frames even if one bit is damaged in each
### Contention | CSMA/CD
Carrier Sense Multiple Access + Collision Detection
- Station keeps listening to channel while sending
- Collision detection
	- minimizes time wasted by collisions

### Token Passing (collision free)
- Special frame (token) circulates between stations in round-robin manner
- Station only emits if it has token
- Station can keep token only for limited time


#### IEEE Stds
 - 802.1 : Gen. introduction
 - 802.2 :...
 - 802.3 : DIX ethernet standard
##### 802.3 Ethernet
- Contention-based MA protocol
- Lower avg time delivery than token ring
##### 802.4 Token Bus
##### 802.5 Token Ring
- Ring topology
- Station does not emit until it gets token
- Guaranteed delivery delay
- Good for stations equally loaded
- Excellent channel efficiency
##### 802.11 WiFi
When tuned to 1 channel
	- Contention-based multiple access protocol
	- General lower avg time delivery than token-ring
##### 802.15 Bluetooh/IoT