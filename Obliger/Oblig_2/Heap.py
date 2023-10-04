def parentOf(i):
    return (i-1)//2
def leftOf(i):
    return 2*i+1
def rightOf(i):
    return 2*i+2

def insert(array, x):
    array.append(x)
    i = len(array-1)

    while i > 0 and array[i] < array[parentOf(i)]:
        array[i], array[parentOf(i)] = array[parentOf(i)], array[i]
        i = parentOf(i)