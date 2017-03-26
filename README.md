# shortestPath

A python script to calculate the shortest driving path


## To run

```python3 shortestPath.py```

## How it works

The file ```data.json``` contains a JSON representation of a tree of nodes with weights, 
as well as some stats on traffic lights.

The program walks this tree and calculates the cost of each path until it reaches each 
leaf node, where it records the ending cost into a global list.

At the end, the program sorts the global list and outputs it shortest first.

## Example run


    File loaded

	Path: start
	  - Current timer: 0 seconds
	  - Drive Time: 0
	  - Timer at end of segment: 0
	  - Traffic Light Cycle: 0.0
	  - Light is RED, waiting 0 seconds for light to change green
	  - Next: start > n1e2

	Path: start > n1e2
	  - Current timer: 0 seconds
	  - Drive Time: 100
	  - Timer at end of segment: 100
	  - Traffic Light Cycle: 3.3333333333333335
	  - Light is RED, waiting 30 seconds for light to change green
	  - Next: start > n1e2 > n2e2

	Path: start > n1e2 > n2e2
	  - Current timer: 130 seconds
	  - Drive Time: 250
	  - Timer at end of segment: 380
	  - Traffic Light Cycle: 12.666666666666666
	  - Light is GREEN, can drive through without waiting
	  - End of the line reached: start > n1e2 > n2e2 = 380 seconds
	  - Next: start > n1e2 > n1e3

	Path: start > n1e2 > n1e3
	  - Current timer: 130 seconds
	  - Drive Time: 130
	  - Timer at end of segment: 260
	  - Traffic Light Cycle: 8.666666666666666
	  - Light is RED, waiting 30 seconds for light to change green
	  - End of the line reached: start > n1e2 > n1e3 = 290 seconds
	  - Next: start > n2e1

	Path: start > n2e1
	  - Current timer: 0 seconds
	  - Drive Time: 85
	  - Timer at end of segment: 85
	  - Traffic Light Cycle: 2.8333333333333335
	  - Light is RED, waiting 30 seconds for light to change green
	  - End of the line reached: start > n2e1 = 115 seconds

	Summary of all paths, sorted shortest to longest
	115 : start > n2e1
	290 : start > n1e2 > n1e3
	380 : start > n1e2 > n2e2
