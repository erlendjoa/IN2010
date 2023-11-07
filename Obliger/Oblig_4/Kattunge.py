

parents = {}
kattNode = input()

inp = input()
while inp != "-1":
    l = inp.split(" ")
    p = l.pop(0)
    for n in l:
        parents[n] = p
    inp = input()

while True:
    try:
        print(kattNode)
        kattNode = parents[kattNode]
    except KeyError:
        break