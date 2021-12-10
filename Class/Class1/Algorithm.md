## Class1

### Prim's Minimum Spanning Tree Algorithm

#### Logic Explanation
```
Step 1: keep track of all the vertices that have been visited and added to the spanning tree.

Step 2: Initially the spanning tree is empty.
    
Step 3: Choose a random vertex, and add it to the spanning tree. This becomes the root node.

Step 4: Add a new vertex, say x, such that x is not in the already built spanning tree. x is connected to the built spanning tree using minimum weight edge. (Thus, x can be adjacent to any of the nodes that have already been added in the spanning tree). Adding x to the spanning tree should not form cycles.

Step 5: Repeat the Step 4, till all the vertices of the graph are added to the spanning tree.

Step 6: Print the total cost of the spanning tree.
```

#### Algorithm breakdown
- Step A:
```text
1. Define key[] array for storing the key value(or cost) of every vertex. Initialize this to (infinity) for all the vertices

2. Define another array booleanvisited[] for keeping a track of all the vertices that have been added to the spanning tree. Initially this will be 0 for all the vertices, since the spanning tree is empty.

3. Define an array parent[] for keeping track of the parent vertex. Initialize this to -1 for all the vertices.

4. Initialize minimum cost, minCost = 0
```
- Step B:
```text
1. Choose any random vertex, say f and set key[f]=0.

2. Since its key value is minimum and it is not visited, add f to the spanning tree.

3. Update minCost = 0 + key[f] = 0, key value is nothing but the cost or the weight of the edge, for (f,d) it is still infinity because they are not directly connected

4. There will be no change in the parent[] because f is the root node.
```

- Step C:
```text
1. The arrays key[] and visited[] will be searched for finding the next vertex.

2. Then update minCost = 0 + key[c] = 0 + 1 = 1, For every adjacent vertex of c, say v, values in key[v] will be updated using the formula:
key[v] = min(key[v], cost[c][v])
```
- Step D:
```text
1. Repeat the Step C for the remaining vertices.

2. Next vertex to be selected is a. And minimum cost will become minCost

3. Then the minimum cost will become minCost

4. Next vertex to be selected, making the minimum cost

5. then the miminum cost would be updated. 

6. Finally when all the vertices have been visited, the algorithm terminate.
```