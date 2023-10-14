import sys, heapq, queue
from collections import defaultdict

class Movie:
    def __init__(self, ttId, tittel, rating):
        self.ttId = ttId
        self.tittel = tittel
        self.rating = rating
        self.nmIds = set()

class Actor:
    def __init__(self, nmId, navn):
        self.nmId = nmId
        self.navn = navn
        self.ttIds = None
    def setttIds(self, ttId):
        self.ttIds = ttId


M = {} # {"ttId":Movie(), "ttId":Movie(), ...}
V = {}
E = set()
G = defaultdict(dict)

with open(sys.argv[2], encoding='utf-8') as f:
    for line in f:
        print("CREATING MOVIE")
        content = line.strip().split("\t")
        M[content[0]] = Movie(content[0], content[1], content[2])

with open(sys.argv[1], encoding='utf-8') as f:
    for line in f:
        print("CREATING ACTOR")
        content = line.strip().split("\t")
        newActor = Actor(content.pop(0), content.pop(0)) #nmId, navn
        movielist = []
        for c in content:
            if c in M:
                movielist.append(M[c].ttId)
                M[c].nmIds.add(newActor.nmId)

        newActor.setttIds(movielist)

        # CREATE VERTICE: Actor()
        V[newActor.nmId] = newActor

for ttId in M:
    print(M[ttId].tittel, len(M[ttId].nmIds))
    for nmId1 in M[ttId].nmIds:
            for nmId2 in M[ttId].nmIds:
                if (nmId1 != nmId2):
                    #print(V[nmId1].navn, V[nmId2].navn, M[ttId].tittel)
                    if (nmId1 != nmId2) and (nmId2, nmId1, M[ttId].ttId) not in E:
                        E.add((nmId1, nmId2, M[ttId].ttId))


print(len(V))
print(len(E))

for t in E:
    G[t[0]][t[1]] = M[t[2]]  # {nmId: {nmId:w}, {nmId:w}, nmId: {nmId:w}, {nmId:w}, ...}
    G[t[1]][t[0]] = M[t[2]]

def DijkstraShortestPath(startId, endId):
    queue = []
    dist = {}
    path = []

    for v in V:
        dist[v] = float(999999999)
    dist[startId] = 0
    heapq.heappush(queue, (0, startId))

    while queue:
        w, u = heapq.heappop(queue)
        print(w, u)
        if u in path:
            return path
        path.append(u)

        if u == endId:
            print("OH")
            return path

        print(len(G[u]))
        for nmKey in G[u]:
            print(V[u].navn + " har spilt med " + V[nmKey].navn + " i filmen " + G[u][nmKey].tittel)

            c = dist[nmKey] + float(G[u][nmKey].rating)
            if c > dist[nmKey]:
                print("og")
                dist[nmKey] = float(G[u][nmKey].rating)
                heapq.heappush(queue, (dist[nmKey], nmKey))

print(len(G))
print(V['nm0000168'].navn, V['nm0000949'].navn)


print(DijkstraShortestPath('nm0000168', 'nm0000949'))