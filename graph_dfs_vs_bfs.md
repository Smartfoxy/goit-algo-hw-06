# Comparison of Graph Traversal Algorithms: DFS and BFS

Two algorithms were used in this work — **DFS (Depth-First Search)** and **BFS (Breadth-First Search)** — to traverse the transportation network graph created in the previous task.  
The starting vertex for both algorithms was **Park**.

## Results

For the same graph, the algorithms produced different traversal orders:

- **DFS**
  _Traversal order_: Park -> University -> City Center -> Train Station -> Shopping Mall -> Residential Area -> Hospital -> Old Town ->

  visits vertices by going as deep as possible along one branch.  
  It follows a single direction until no unvisited neighbors remain, and only then backtracks.  
  Because of this, DFS may produce long sequences of nodes that do not represent the shortest paths.

- **BFS**
  _Traversal order_: Park -> Residential Area -> University -> Shopping Mall -> Hospital -> Train Station -> City Center -> Old Town ->

  explores the graph level by level — first all vertices one edge away from the start, then the next layer, and so on.  
  Therefore, BFS always finds the shortest paths in an unweighted graph.

## Conclusions

Overall, it can be said that:

- **BFS** guarantees the shortest paths (in terms of number of edges) for unweighted graphs;
- **DFS** explores the graph in depth and may produce longer, non-optimal paths;
- the difference in traversal sequences is explained by the fundamentally different strategies:  
  DFS goes deep, while BFS expands in layers.

The obtained results fully correspond to the theoretical behavior of these algorithms.
