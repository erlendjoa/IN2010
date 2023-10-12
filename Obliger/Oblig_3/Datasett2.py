import sys, heapq

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

with open(sys.argv[2], encoding='utf-8') as f:
    for line in f:
        print("CREATING MOVIE")

        content = line.strip().split("\t")
        try:
            M[content[0]] = Movie(content[0], content[1], content[2])
        except IndexError:
            print("NO")

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
                #print(V[nmId1].navn, V[nmId2].navn, M[ttId].tittel)
                if nmId1 != nmId2:
                    E.add((V[nmId1], V[nmId2], M[ttId].rating))


print(len(V))
print(len(E))


def DijkstraShortestPath(s):
    queue = [] 
    dist = {}
    for v in V:
        dist[v] = 9999999999999
    dist[s.nmId] = 0
    heapq.heappush(queue, s, dist[s.nmId])

    while len(queue) > 0:
        s = heapq.heappop(queue)