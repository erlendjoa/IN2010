import math;

def selvbalanser(L):
    A = []
    mid = L.pop((len(L))//2)
    A.append(mid)
    insertRec(L[math.ceil((len(L))/2):], A)
    insertRec(L[:math.ceil((len(L))/2)], A)
    return A

def insertRec(L, A):
    if len(L) == 0:
        return
    mid = L.pop(len(L)//2)
    A.append(mid)
 
    if (len(L) == 2):
        A.append(L.pop(1))
        A.append(L.pop(0))
    else:
        insertRec(L[math.ceil((len(L))/2):], A)
        insertRec(L[:math.ceil((len(L))/2)], A)


arr = []
inp = input()
while inp != "":
    arr.append(int(inp))
    inp = input()
for i in selvbalanser(arr):
    print(i)