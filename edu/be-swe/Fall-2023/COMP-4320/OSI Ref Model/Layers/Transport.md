- Accepts data from above -> splits into smaller units -> pass to [[Network]] layer -> ensure all pieces arrive correctly at the other end
- Handles addressing (port numbers), error control, congestion control, flow control!!
- Provides 2 services to [[Session]] layer (type determined when conn. established)
	1. Error-free point->point channel that delivers data in original order
	2. Transports isolated messages with no guarantee of in-order delivery
