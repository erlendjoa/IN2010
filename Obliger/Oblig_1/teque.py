arr = []

def teque(s):
    l = s.split(" ")
    n = int(l[1])

    if l[0] == "push_back":
        arr.append(n)
    elif l[0] == "push_front":
        arr.insert(0, n)
    elif l[0] == "push_middle":
        arr.insert((len(arr)+1)//2, n)
    else:
        print(arr[n])

for i in range(int(input())):
    teque(input())