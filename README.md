# Maze Search

Objective: Finding the optimal path from a Maze entrance to exit using Breadth-First Search (BFS), Uniform-Cost Search (UCS), and A* Search (A*).

**Actions:**
The 18 actions are defined as follows. They are roughly divided as “straight-move” and “diagonal-move” actions. The six straight-move actions are X+, X-, Y+, Y-, Z+, Z-, and they allow the agent to move in a straight-line to the next grid point. The diagonal-move actions are further defined on xy, xz, and yz planes, respectively. For example, the actions X+Y+, X+Y-, X-Y+, and X-Y-, are those moves diagonally on the xy plane. Similarly, the actions X+Z+, X+Z-, X-Z+, and X-Z-, are those moves diagonally on the xz plane. Finally, the actions Y+Z+, Y+Z-, Y-Z+, and Y-Z-, are those moves diagonally on the yz plane. Not all actions may be available for a given grid location, and not all grid locations may have actions. For clear format purpose, we name or encode these actions as follows:

| Act    | Code |
|--------|------|
| X+     | 1    |
| X-     | 2    |
| Y+     | 3    |
| Y-     | 4    |
| Z+     | 5    |
| Z-     | 6    |
| X+Y+   | 7    |
| X+Y-   | 8    |
| X-Y+   | 9    |
| X-Y-   | 10   |
| X+Z+   | 11   |
| X+Z-   | 12   |
| X-Z+   | 13   |
| X-Z-   | 14   |
| Y+Z+   | 15   |
| Y+Z-   | 16   |
| Y-Z+   | 17   |
| Y-Z-   | 18   |

**Search Algorithms:**

- Breadth-first search (BFS): In BFS, each allowed move from one location to any of its neighbors counts for a unit path cost of 1. For simplicity, moving diagonally costs 1 as well even though moving along a diagonal is a bit longer than moving along the North/South, East/West, and Up/Down directions.
 
- Uniform-cost search (UCS): In UCS, unit path costs are computed in any of the 2D planes XY, XZ, YZ, on which the agent is moving. Let's assume that a grid location’s center coordinates projected to a 2D plane are spaced by a 2D distance of 10 units on X and Z plane respectively. That is, on the XZ plane, move from a grid location to one of its 4-connected straight neighbors incurs a unit path cost of 10, while a diagonal move to a neighbor incurs a unit path cost of ​14 as an approximation to 10​√𝟐 ​when running UCS.
 
- A* search (A*): In A*, an approximate integer unit path cost is computed for each move as in the UCS case (unit cost of 10 when moving straight on a plane, and unit cost of 14 when moving diagonally). 


**Input:** 
 input.txt file formatted as follows:
 - First Line: Instruction of which algorithm to use, as a string: BFS, UCS, or A*.
 - Second Line: Three strictly positive 32-bit integers separated by one space character, for the size of X, Y, and Z dimensions, respectively.
 - Third line: Three non-negative 32-bit integers for the entrance grid location.
 - Fourth line: Three non-negative 32-bit integers for the exit grid location.
 - Fifth line: A strictly positive 32-bit integer N, indicating the number of grids in the maze where there are actions available.
 - Next N lines: Three non-negative 32-bit integers separated by one space character, for the location of the grid, followed by a list of actions that are available at this grid. The grid location is guaranteed to be legal and within the maze.

 For example:
 
 A*
 
 100 200 100 00 0

 33 0
 
 4
 
 0 0 0 7
 
 1 1 0 7 10
 
 2 2 0 7 10 
 
 3 3 0 10

In this example, the 3D maze is of size 100 x 200 x 100 (​specifically, points range from (0,0,0) to (99,199,99)​), the entrance grid location is at (0,0,0), and the exit grid location is at (3,3,0). In this maze, there are 4 grid locations that have actions and they are specified in the next four lines. ​Namely, the grid (0,0,0) has one action X+Y+ (encoded as 7); the grid (1,1,0) has two actions X+Y+ and X-Y- (encoded as 7 and 10); the grid (2,2,0) has two actions X+Y+ and X-Y- (encoded as 7 and 10); and the grid (3,3,0) has one action X-Y- (encoded as 10).

**Output:** 
Returns the shortest possible operational path length if a path is possible, otherwise returns 'FAIL'.

 - First line: A single integer C, indicating the total cost of the found solution. If no solution was found (the exit grid location is unreachable from the given entrance, then 'FAIL'.
 - Second line: A single integer N, indicating the total number of steps in the solution including the starting position.
 - N lines: The steps in the solution travelling from the entrance grid location to the exit grid location as were given in the input.txt file. One line per step with cost. Each line contains a tuple of four integers: X, Y, Z, Cost, separated by a space character, specifying the grid location with the single step cost to visit that grid location by the agent from its last grid during its traveling from the entrance to the exit.

For example (corresponding to the input above):

42 4

0 0 00

1 1 0 14

2 2 0 14

3 3 0 14
