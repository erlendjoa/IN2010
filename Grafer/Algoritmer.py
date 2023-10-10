
list = []
V = set()
E = {}
W = {}

def BuildGraph(list):
    for i in range(len(list)):
        u = list[i][0]
        v = list[i][0]
        V.add(u)
        V.add(v)
        E[u].add(v)
        E[v].add(u)
        W[v,u] = int(list[i][2])
    return V, E, W

def DFSFull():
    visited = set()
    result = []
    for v in V:
        if v not in visited:
            DFSVisit(v, visited, result)
    return result

def DFSVisit(u, visited, result):
    visited.add(u)
    result.append(u)
    for (u, v) in E:
        if v not in visited:
            DFSVisit(v, visited)