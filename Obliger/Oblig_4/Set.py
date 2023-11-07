
class HashSet:
    def __init__(self):
        self.arr = [""] * 11
        self.maxIndex = 11
        self.sizeOf = 0

    def hash(self, n):
        return ((n*31)%self.maxIndex)

    def insert(self, n):
        hashed = self.hash(n)
        if self.arr[hashed] == n:
            return
        elif self.arr[hashed] == "":
            self.arr[hashed] = n
        else:
            if not isinstance(self.arr[hashed], list):
                prev = self.arr[hashed]
                self.arr[hashed] = [prev]
            if n not in self.arr[hashed]:
                self.arr[hashed].append(n)
        self.sizeOf += 1

    def remove(self, n):
        hashed = self.hash(n)
        if isinstance(self.arr[hashed], list):
            for i in range(len(self.arr[hashed])):
                cur = self.arr[hashed][i]
                if cur == n:
                    self.arr[hashed].remove(n)
                    if len(self.arr[hashed]) == 1:
                        self.arr[hashed] = self.arr[hashed][0]
                    elif len(self.arr[hashed]) == 0:
                        self.arr[hashed] = ""
                    break
        else:
            self.arr[hashed] = ""
        self.sizeOf -= 1

    def contains(self, n):
        hashed = self.hash(n)
        if isinstance(self.arr[hashed], list):
            for key in self.arr[hashed]:
                if key == n:
                    return True
        return self.arr[hashed] == n
    
    def size(self):
        return self.sizeOf


def hashSet(s):
    l = s.split(" ")
    if len(l) > 1:
        n = int(l[1])

        if l[0] == "insert":
            set.insert(n)
        elif l[0] == "contains":
            print(set.contains(n))
        elif l[0] == "remove":
            set.remove(n)
    else:
        print(set.size())


set = HashSet()
for i in range(int(input())):
    hashSet(input())


"""
b)
    Tidsbruken på denne implementasjonen basert på 
    seperate chaining hashing er som regel raskere enn
    min implementasjon av et binært søketre fordi
    kjøretidskompleksiteten til hashsettet har 
    forvented amortisert kjøretid på O(1) ved
    alle funksjoner, hvor bst har forventet amortisert
    kjøretid på O(logn) og værste O(n).
    Hvis treet er lite vil det muligens være raskere, avhengig
    om det er selv-balanserende og avhengig av rekkefølge som
    er satt inn for begge datastrukturene.
"""