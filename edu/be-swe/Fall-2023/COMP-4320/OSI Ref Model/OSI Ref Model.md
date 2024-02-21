# Open Systems Interconnection
* Developed by ISO
* Very thorough, great model, but **high paywall** to access standards
* No viable stack implementation

## Principles
1. A layer should be created where a different abstraction is needed
2. Each layer should perform a well-defined function
3. Function of each layer should be chosen with an eye towards defining intl. standardized protocols
4. Minimal information flow across interfaces
5. There should be a large enough number of layers s.t. distinct functions are not thrown into the same layer out of necessity
	1. Should be small enough s.t. architecture is not unwieldy.

![[OSI Ref Model.canvas|OSI Ref Model]]
### Two Kinds of Layers
* End->end: [[BE SWE/Fall 2023/COMP-4320/OSI Ref Model/Layers/Application]], [[Presentation]], [[Session]], [[BE SWE/Fall 2023/COMP-4320/OSI Ref Model/Layers/Transport]]
* Point->point: [[Network]], [[Data Link]], [[Physical]]

### Statistical Multiplexing
* Sharing based on the statistics of demands