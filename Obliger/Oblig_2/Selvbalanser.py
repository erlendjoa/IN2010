import math;

def selvbalanser(L):
    A = []
    mid = L.pop((len(L)-1)//2)
    A.append(mid)
    print(L, mid)

    insertRec(L[(len(L)-1)//2:], A)
    insertRec(L[:(len(L)-1)//2], A)
    return A
    

def insertRec(L, A):
    print(L, (len(L)-1)//2)
    mid = L.pop((len(L)-1)//2)
    A.append(mid)

    if len(L) > 1:
        insertRec(L[(len(L)-1)//2:], A)
        insertRec(L[:(len(L)-1)//2], A)
    if len(L) == 1:
        A.append(L[0])

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(selvbalanser(arr))