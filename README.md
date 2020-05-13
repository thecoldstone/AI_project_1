# Rectangular Partition Surveillance

  ### Search methods
  ```
    - Simple
    - Breadth First Search (BFS)
    - Depth First Search (DFS)
    - Iterative Deepening Search (IDS)
    - A* Search (A*)
    - Branch&Bound (B&B)
  ```

  ### Build
  
  ```bash
  git clone https://github.com/thecoldstone/AI_project_1
  python3 main.py file [method] [o]
  ```
  
  ##### Methods
  
  Without [method] you call simple search
  
  The following search methods:
  
  | Method | Search Method |
  | ---  | --- |
  |1     | BFS |
  |2     | DFS |
  |2 o   | Optimized DFS|
  |3     |(IDS)|
  |4     |(A*)|
  |5     |(B&B)|
  
  Flag [o] server for optimized version for DFS Algorithm
   
  
  ### Hierarchy
  
  ```
    - main.py   
    - parser.py    
    - Search/        
    --- solver.py   
    --- node.py     
    --- guard.py
    --- Algorithms/
    ----- astar.py
    ----- bfs.py
    ----- branch_and_bound.py
    ----- dfs.py
    ----- ids.py
    ----- simple.py
  ```
   
  ### Contributors
  ```
    - Nikita Zhukov
    - Angelo
    - Bernardo
  ```
      
     