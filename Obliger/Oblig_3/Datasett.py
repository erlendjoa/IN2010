import sys, heapq

class Movie:
    def __init__(self, ttId, tittel, rating):
        self.ttId = ttId
        self.tittel = tittel
        self.rating = rating

class Actor:
    def __init__(self, nmId, navn):
        self.nmId = nmId
        self.navn = navn
        self.ttIds = None
    def setttIds(self, ttId):
        self.ttIds = ttId


allActors = {}
allMovies = {}

V = {}
E = set()

with open(sys.argv[2], encoding='utf-8') as f:
    for line in f:
        print("CREATING MOVIE")

        content = line.strip().split("\t")
        try:
            allMovies[content[0]] = Movie(content[0], content[1], content[2])
        except IndexError:
            print("NO")

with open(sys.argv[1], encoding='utf-8') as f:
    for line in f:
        print("CREATING ACTOR")

        content = line.strip().split("\t")

        newActor = Actor(content.pop(0), content.pop(0)) #nmId, navn
        movielist = []
        for c in content:

            if c in allMovies:
                movielist.append(allMovies[c])
                # CREATE EDGE: (Actor(), Movie(), float)
                E.add((newActor, allMovies[c], allMovies[c].rating))

                if c not in V:
                    V[c] = []
                V[c].append(newActor)


        newActor.setttIds(movielist)
        # CREATE VERTICE: Actor()
        V[newActor.nmId] = newActor

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
        