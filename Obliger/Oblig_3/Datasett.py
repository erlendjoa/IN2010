import sys, heapq
from collections import defaultdict, deque

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


M = {} # {"ttId": Movie(), "ttId": Movie(), ...}
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
    for nmId1 in M[ttId].nmIds:
            for nmId2 in M[ttId].nmIds:
                if (nmId1 != nmId2):
                    if (nmId1 != nmId2) and (nmId2, nmId1, M[ttId].ttId) not in E:
                        E.add((nmId1, nmId2, M[ttId].ttId))

for t in E:
    G[t[0]][t[1]] = M[t[2]]  # {nmId: {nmId:w}, {nmId:w}, nmId: {nmId:w}, {nmId:w}, ...}
    G[t[1]][t[0]] = M[t[2]]


def bfs_shortest_paths_from(s):
    parents = {s : None}
    queue = deque([s])

    while len(queue) > 0:
        u = queue.popleft()
        for v in G[u]:
            if v not in parents:
                parents[v] = u
                queue.append(v)

    return parents

def bfs_shortest_path_between(s, t):
    parents = bfs_shortest_paths_from(s)
    v = t
    path = []

    if t not in parents:
        return path

    while v:
        path.append((v, parents[v]))
        v = parents[v]
    
    for nmIdT in path[::-1]:
        try:
            print(f"===[ {G[nmIdT[0]][nmIdT[1]].tittel} ({G[nmIdT[0]][nmIdT[1]].rating}) ] ===> {V[nmIdT[0]].navn}")
        except KeyError:
            print(V[nmIdT[0]].navn)


def dijkstra_chillest_path(s, t):
    parents = {}
    parents = {s : None}

    queue = []
    dist = {}
    for v in V:
        dist[v] = float('inf')
        #heapq.heappush(queue, (dist[v], v))
    dist[s] = 0
    heapq.heappush(queue, (dist[s], s))

    while len(queue) > 0:
        w, u = heapq.heappop(queue)

        if u == t:
            path = []
            while u:
                print("!!!")
                path.append((u, parents[u]))
                u = parents[u]
            for nmIdT in path[::-1]:
                try:
                    print(f"===[ {G[nmIdT[0]][nmIdT[1]].tittel} ({G[nmIdT[0]][nmIdT[1]].rating}) ] ===> {V[nmIdT[0]].navn}")
                except KeyError:
                    print(V[nmIdT[0]].navn)
        

        for v, e in hent_chilleste_actors(u):
            c = w + e
            if c < dist[v]:
                parents[v] = u
                dist[v] = c
                heapq.heappush(queue, (c, v))

                
def hent_chilleste_actors(u):
    arr = deque()
    for v in G[u]:
        e = float(G[u][v].rating)

        if len(arr) == 0:
            arr.append((v, e))
        else:
            for i in range(len(arr)):
                if e < arr[i][1]:
                    arr.insert(i, (v, e))
                    break
                if i == len(arr)-1:
                    arr.append((v, e))
    return arr
'''
def bfs_chillest_paths_from(s):
    parents = {s : None}
    queue = deque([s])

    while len(queue) > 0:
        u = queue.popleft()
        for v, w in hent_chilleste_actors(u):
            if v not in parents:
                parents[v] = u
                queue.append(v)

    return parents

def bfs_chillest_path_between(s, t):
    parents = bfs_chillest_paths_from(s)
    v = t
    path = []

    if t not in parents:
        #print("OOPSIE")
        return path

    while v:
        path.append((v, parents[v]))
        v = parents[v]
    
    for nmIdT in path[::-1]:
        try:
            print(f"===[ {G[nmIdT[0]][nmIdT[1]].tittel} ({G[nmIdT[0]][nmIdT[1]].rating}) ] ===> {V[nmIdT[0]].navn}")
        except KeyError:
            print(V[nmIdT[0]].navn)
'''

print("VERTICES: " + str(len(V)))
print("EDGES: " + str(len(E)))

bfs_shortest_path_between('nm2255973', 'nm0000460')
bfs_shortest_path_between('nm0424060', 'nm8076281')
bfs_shortest_path_between('nm4689420', 'nm0000365')
bfs_shortest_path_between('nm0000288', 'nm2143282')
bfs_shortest_path_between('nm0637259', 'nm0931324')

bfs_shortest_path_between('nm0000313', 'nm1107001')
dijkstra_chillest_path("nm0000313", "nm1107001")