from collections import deque

V = set() # set of vertices
E = {} # dict of edges aka: {"A":("B","C"), ...}


def BFSShortestPath(s):
    parents = {}
    queue = deque()

    queue.append(s)
    parents[s] = None

    while len(queue) > 0:
        u = queue.popleft()
        for v in E[u]:
            if v not in parents:
                parents[v] = u