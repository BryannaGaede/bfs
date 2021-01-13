# Breadth First Search in Python
## Mine-Finder
##### project idea from https://www.techiedelight.com/find-shortest-distance-every-cell-landmine-maze/
<br>

### Problem:

#### Given an two-dimentional array containing open squares ('O'), blocked squares ('X') and a squares with mines ('M'), find the minimun number of moves, horizontal and vertical, it takes to reac a mine from each square. An example input would be a text file containing the following information:

O M O O X <br>
O X X O M <br>
O O O O O <br>
O X X X O <br>
O O M O O <br>
O X X M O <br>

#### The resulting output would be as follows:

1 0 1 2 -1 <br>
2 -1 -1 1 0 <br>
3 4 3 2 1 <br>
3 -1 -1 -1 2 <br>
2 1 0 1 2 <br>
3 -1 -1 0 1 <br>

### Solution:

The solution to this problem is written in Python and used breadth first search. <br>
2-3 command line arguments are used, input file, output file and optional 1 for debugging messages to print.