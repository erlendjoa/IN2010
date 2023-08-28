arr = []

def pushFront(n):
    current = arr[i]
    arr[i] = n
    for i in range(0, len(arr)-1):
        next = arr[i+1]
        

        

def teque(s):
    n = int(s[len(s)-1])

    if s[:-1] == "push_back":
        arr.append(n)
    elif s[:-1] == "push_front":
        pushFront(n)
    else:
        pushMiddle(n)

        

inpInt = input()
inp1 = input()
teque(inp1)