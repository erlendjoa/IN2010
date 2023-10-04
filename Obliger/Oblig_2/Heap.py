
def parentOf(i):
    return (i-1)//2
def leftOf(i):
    return 2*i+1
def rightOf(i):
    return 2*i+2

def insert(array):
    for i in range(len(array)):
        while i > 0 and array[i] < array[parentOf(i)]:
            array[i], array[parentOf(i)] = array[parentOf(i)], array[i]
            i = parentOf(i)
    return array

arr = []
inp = input()
while inp != "":
    arr.append(int(inp))
    inp = input()

for i in insert(arr):
    print(i)