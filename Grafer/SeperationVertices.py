import math


V = set()
E = set()

A = "A"
V.add(A)
V.add("B")
V.add("C")
V.add("D")

E.add(("A", "B"))
E.add(("B", "A"))

E.add(("B", "C"))
E.add(("C", "B"))

E.add(("C", "D"))
E.add(("D", "C"))

E.add(("B", "D"))
E.add(("D", "B"))

low = {}
depth = {}
seps = set()

def SeperationVertices():
    u = A
    depth[u] = 0
    low[u] = 0
    children = 0

    for (u, v) in E:
        if v not in depth:
            SepRec(u, v, 1)
            children += 1
    if children > 1:
        seps.add(u)

def SepRec(p, u, d):
    depth[u] = d
    low[u] = d

    for (u, v) in E:
        if v == p:
            continue
        if v == u:
            low[u] = math.min(low[u], low[v])
            continue
        SepRec(u, v, d+1)
        low[u] = math.min(low[u], low[v])
        if depth[u] <= low[v]:
            seps.add(u)

SeperationVertices()