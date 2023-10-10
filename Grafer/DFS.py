list = []
V = set()
E = {}
W = {}

def DFSFull():
    visited = set()
    orderResult = []
    for v in V:
        if v not in visited:
            DFSVisit(v, visited, orderResult)
    return orderResult

def DFSVisit(u, visited, result):
    visited.add(u)
    result.append(u)
    for (u, v) in E:
        if v not in visited:
            DFSVisit(v, visited)