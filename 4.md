# ExpNo 4 : Implement A* search algorithm for a Graph

## Name: Sowmya V  
## Register Number: 212222110045 

### AIM:
To Implement A * Search algorithm for a Graph using Python 3.

### Algorithm:
1.  Initialize the open list
2.  Initialize the closed list put the starting node on the open list (you can leave its f at zero)
3.  while the open list is not empty
    - find the node with the least f on the open list, call it "q"
    - pop q off the open list
    - generate q's 8 successors and set their parents to q
    - for each successor
4. if successor is the goal, stop search
5. else, compute both g and h for successor
    - successor.g = q.g + distance between successor and q
    - successor.h = distance from goal to successor (This can be done using many  ways, we will discuss three heuristics-  Manhattan, Diagonal and Euclidean  Heuristics)
    - successor.f = successor.g + successor.h
    - if a node with the same position as successor is in the OPEN list which has a lower f than successor, skip this successor
    - if a node with the same position as successor  is in the CLOSED list which has a lower f than successor, skip this successor otherwise, add  the node to the open list end (for loop)
    - push q on the closed list end (while loop)

## PROGRAM:
```
from collections import defaultdict
H_dist = {}

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}              
    parents = {}        
    
    g[start_node] = 0
    parents[start_node] = start_node
    
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n is None:
            print("Path does not exist!")
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path

        open_set.remove(n)
        closed_set.add(n)
        
        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

    print("Path does not exist!")
    return None

def get_neighbors(v):
    return Graph_nodes[v]

def heuristic(n):
    return H_dist[n]

graph = defaultdict(list)
n, e = map(int, input().split())

for i in range(e):
    u, v, cost = map(str, input().split())
    t = (v, float(cost))
    graph[u].append(t)
    t1 = (u, float(cost))
    graph[v].append(t1)

for i in range(n):
    node, h = map(str, input().split())
    H_dist[node] = float(h)

print(H_dist)
Graph_nodes = graph
print(graph)
aStarAlgo('A', 'J')
```

### Sample Graph I:
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/b1377c3f-011a-4c0f-a843-516842ae056a)

### Sample Input for graph 1:
```
10 14
A B 6
A F 3
B D 2
B C 3
C D 1
C E 5
D E 8
E I 5
E J 5
F G 1
G I 3
I J 3
F H 7
I H 2
A 10
B 8 
C 5 
D 7 
E 3 
F 6 
G 5 
H 3 
I 1 
J 0 
```
### Output:
![image](https://github.com/user-attachments/assets/54ce6909-7dfa-4f05-bdd7-14c0660e7510)

### Sample Graph II
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/acbb09cb-ed39-48e5-a59b-2f8d61b978a3)

### Sample Input
```
6 6 
A B 2
B C 1
A E 3
B G 9
E D 6
D G 
A 11
B 6 
C 99
E 7 
D 1 
G 0 
```
### Sample Output</h2>
![image](https://github.com/user-attachments/assets/bf6d02da-656e-432f-aa9b-f962a335899b)

### Result:
Thus, the python program to implement A * Search algorithm for a Graph was executed successfully.
