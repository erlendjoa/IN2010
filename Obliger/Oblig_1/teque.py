

arr = []  

def pushFront(n):
    if len(arr) == 0:
        arr.append(n)
        return
    
    current = arr[0]
    arr[0] = n
    for i in range(len(arr)):
        if (i+1 == len(arr)):
            arr.append(current)
            return
        next = arr[i+1]
        arr[i+1] = current
        current = next

def pushMiddle(n):
    if (len(arr) == 0) or (len(arr) == 1):
        arr.append(n)
        return
    
    mid = (len(arr)+1//2)-1
    current = arr[mid]
    arr[mid] = n

    for i in range(mid, len(arr)):
        if (i+1 == len(arr)):
            arr.append(current)
            return
        next = arr[i+1]
        arr[i+1] = current
        current = next

def teque(s):
    l = s.split(" ")
    n = int(l[1])

    if l[0] == "push_back":
        arr.append(n)
    elif l[0] == "push_front":
        arr.insert(0, n)
        #pushFront(n)
    elif l[0] == "push_middle":
        arr.insert((len(arr)+1)//2, n)
        #pushMiddle(n)
    else:
        print(arr[n])

for i in range(int(input())):
    teque(input())