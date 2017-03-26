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


