import math;

def selvbalanser(L):
    A = []
    mid = L.pop((len(L))//2)
    A.append(mid)
    print(L, mid)

    insertRec(L[math.ceil((len(L))/2):], A)
    insertRec(L[:math.ceil((len(L))/2)], A)
    return A


def insertRec(L, A):
    if len(L) == 0:
        return
    mid = L.pop(len(L)//2)
    A.append(mid)
    print(L, mid)
 
    if (len(L) == 2):
        A.append(L.pop(1))
        A.append(L.pop(0))
        print(L)
    else:
        insertRec(L[math.ceil((len(L))/2):], A)
        insertRec(L[:math.ceil((len(L))/2)], A)


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(selvbalanser(arr))