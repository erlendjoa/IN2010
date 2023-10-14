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

print(V['nm0000168'].navn, V['nm0000949'].navn)


def DijkstraShortestPath(startId, endId):
    queue = []
    dist = {}
    path = []

    for v in V:
        dist[v] = float('inf')
        heapq.heappush(queue, (dist[v], v))
    dist[startId] = 0
    heapq.heappush(queue, (dist[startId], startId))

    while len(queue) > 0:
        u = heapq.heappop(queue)
        # u[0] <- weight
        # u[1] <- nmId
        if u in path:
            continue
        
        path.append(u[1])

        if u[1] == endId:
            return path

        for nmKey in G[u[1]]:
            print(V[u[1]].navn + " har spilt med " + V[nmKey].navn + " i filmen " + G[u[1]][nmKey].tittel)

            c = ( dist[nmKey] + float(G[u[1]][nmKey].rating)) 
            if c > dist[nmKey]:
                dist[nmKey] = float(G[u[1]][nmKey].rating)
                heapq.heappush(queue, (dist[nmKey], nmKey))


print(DijkstraShortestPath('nm0000168', 'nm0000949'))