list = []
V = set()
E = set()
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