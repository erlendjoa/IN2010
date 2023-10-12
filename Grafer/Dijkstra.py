import heapq;

V = set() # vertices ("A", "B", ...)
E = {} # edges {"A":("A","B"), ...}
W = {} # edge-weight {("A","B"): 2, ("A","C"): 4, ...}

def Dijkstra(s): # s <- startnode
    queue = []
    dist = {}
    
    for v in V:
        dist[v] = 999999

    dist[s] = 0
    heapq.heappush(queue, (dist[s], v))

    while len(queue) > 0:
        u = heapq.heappop(queue)
        for (u, v) in E:
            c = dist[u] + W[(u, v)]
            if c < dist[v]:
                dist[v] = c
                heapq.heappush(queue, (c, v))
    
    return dist