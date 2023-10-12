import heapq;

V = set() # vertices ("A", "B", ...)
E = () # edges {("A","B"), ("A","C"), ...}
W = {} # edge-weight {("A","B"): 2, ("A","C"): 4, ...}

def Prim(s):
    queue = []
    parents = {}

    heapq.heappush(queue, (0, (None, s)))
    
    while len(queue) > 0:
        (p, u) = heapq.heappop(queue)
        if u not in parents:
            parents[u] = p
            for (u, v) in E:
                heapq.heappush(queue, (W[(u, v)], (u, v)))
                
    return parents