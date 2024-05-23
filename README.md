# A* Search

A group of researchers are being chased by zombies through a dark forest late at night. They<br>
come to a rope bridge over a ravine. If they can all get over the bridge before the zombies arrive,<br>
they will survive.<br>
At most two people can cross at a time. A person or pair of people can only cross when they<br>
have a flashlight with them. The group has only a single flashlight among them, so one person<br>
must bring the flashlight back across the bridge to the starting side before anyone else can<br>
cross. Each pair moves at the pace of its slowest member, i.e., the Undergrad and the Professor<br>
will take 10 minutes to cross if they go together.<br>
Each person moves at a different pace:<br>
- The Undergrad can cross the bridge in 1 minute.<br>
- The Grad Student can cross the bridge in 2 minutes.<br>
- The Postdoc can cross the bridge in 5 minutes.<br>
- The Professor can cross the bridge in 10 minutes.<br>
How can the whole group get to the other side of the bridge in the shortest possible time?<br>

## What is an A* Search?

A* Search algorith is used for path finding and traversal.<br>
It combines the strength of Dijkstras's algorithm and Greedy Best-First-Search to find the shortest path from a start node to a goal node.<br>
A* Search is complete meaning if a solution exists it will find one, and it is optimal meaning it will always find the shortest path if it useses an admissible huristic function.

## How does A* Search work?

A* picks the path with the lowest f-value first.

Function for f-value: f(n) = g(n) + h(n)
where:
g(n) is the cost function that shows the exact cost to reach node n from the start node.
h(n) is a heuristic funstion that gives an estimate of the cost to reach the goal node form a node n.


## Installation

Make a clone of the bridge_&_torch.py file in the repository.

Make sure you are using the correct Python version (ideally Python 3).<br>
Run the bridge_&_torch.py file. No other file is needed.

## Output

After successfully running the code in the terminal, it will show "testing...", Which might take some time as it is finding the best path.<br>
After that it will show some messages that says the testing has been done succesfully.<br>
Then it will show you the output or the path with the lowest cost and the total cost at the end.

## Not functioning?
If you run into difficulties or errors in the code please feel free to reach out.<br>
Email: contact@shahmeer.xyz