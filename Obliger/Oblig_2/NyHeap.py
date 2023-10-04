# [3, 1, 6, 0, 2, 4, 8]
# ønsket resultat:
# [3, 6, 8, 4, 1, 2, 0]

import heapq
import math


def parentOf(i):
    return (i-1)//2
def leftOf(i):
    return math.ceil(2*i+1)
def rightOf(i):
    return math.ceil(2*i+2)


def insert(L):
    A = []
    mid = L.pop((len(L))//2)
    A.append(L.pop(mid))
    insertRec(L[math.ceil((len(L))/2):], A)
    insertRec(L[:math.ceil((len(L))/2)], A)

def insertRec(L, A):
    

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(rightOf(1))
print(heap)

