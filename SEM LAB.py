# 1. PEAS DESCRIPTION

def percept(self, agent):
    return agent.location, self.status[agent.location]

def execute_action(self, agent, action):
    if action == "Right":
        agent.location = room_B
        agent.performance -= 1
    elif action == "Left":
        agent.location = room_A
        agent.performance -= 1
    elif action == "suck":
        self.status[agent.location] == "dirty"
        agent.performance += 10
        self.status[agent.location] = "clean"

# 2. DFS

def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for neighbour in graph[start]:
        if visited[neighbour]==False:
            dfs(graph,neighbour,visited,path)
            visited[neighbour]=True
    return path

# 3. BFS

def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

# 4.  A*

def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
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
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

#5.  SIMPLE HILL CLIMBING

def SimpleHillClimbing(answer):
    best=generate_random_solution(answer)
    best_score=evaluate(best,answer)
    while True:
        if best_score==0:
            print("Score:",best_score," Solution : ","".join(best))
            break
        new_solution=mutate_solution(list(best))
        score=evaluate(new_solution,answer)
        if score<best_score:
            best=new_solution
            best_score=score

#6.  CSP

from itertools import permutations
def solvecrypt():
    for perm in permutations(range(10),9):
        C,R,O,S,A,D,N,G,E=perm
        if C==0 or R==0:
            continue
        CROSS=C*10000+R*1000+O*100+S*10+S
        ROADS=R*10000+O*1000+A*100+D*10+S
        DANGER=D*100000+A*10000+N*1000+G*100+E*10+R
        if CROSS+ROADS==DANGER:
            print("CROSS", CROSS)
            print("ROADS", ROADS)
            print("DANGER", DANGER)
solvecrypt()

#7. MIN MAX SEARCH ALGORITHM

def max():
    maxv = -2
    px = None
    py = None
    result = is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j] == '.':
                current_state[i][j] = 'O'
                (m, min_i, min_j) = min()
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                current_state[i][j] = '.'
    return (maxv, px, py)
def min():
    minv = 2
    qx = None
    qy = None
    result = is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j] == '.':
                current_state[i][j] = 'X'
                (m, max_i, max_j) = max()
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                current_state[i][j] = '.'
    return (minv, qx, qy)

#8. ALPHA BETA  PRUNING

def max_alpha_beta(self, alpha, beta):
    maxv = -2
    px = None
    py = None
    result = self.is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if self.current_state[i][j] == '.':
                self.current_state[i][j] = 'O'
                (m, min_i, min_j) = self.min_alpha_beta(alpha, beta)
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                self.current_state[i][j] = '.'
                if maxv >= beta:
                    return (maxv, px, py)

                if maxv > alpha:
                    alpha = maxv
    return (maxv, px, py)

def min_alpha_beta(self, alpha, beta):
    minv = 2
    qx = None
    qy = None
    result = self.is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == '.':
        return (0, 0, 0)
    for i in range(0, 3):
        for j in range(0, 3):
            if self.current_state[i][j] == '.':
                self.current_state[i][j] = 'X'
                (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                self.current_state[i][j] = '.'
                if minv <= alpha:
                    return (minv, qx, qy)
                if minv < beta:
                    beta = minv
    return (minv, qx, qy)



