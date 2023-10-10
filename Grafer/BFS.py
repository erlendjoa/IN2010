from collections import deque;

list = []
V = set()
E = {}
W = {}

def BFS(s): # s = source node
    visited = set()
    queue = deque() # stack
    queue.append(s)
    orderResult = []

    visited.add(s)

    while len(queue) > 0:
        u = queue.popleft()
        orderResult.append(u)
        for v in E[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                
    return orderResult