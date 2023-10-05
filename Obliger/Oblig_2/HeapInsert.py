import heapq

def heapInsert(A):
    if len(A) == 1:
        print(heapq.heappop(A))
    else:
        T = []
        for i in range(len(A)//2):
            heapq.heappush(T, heapq.heappop(A))
        print(heapq.heappop(A))

        if len(A) > 0:
            heapInsert(A)
        if len(T) > 0:
            heapInsert(T)

arr = []
inp = input()
while inp != "":
    heapq.heappush(arr, int(inp))
    inp = input()
heapInsert(arr)