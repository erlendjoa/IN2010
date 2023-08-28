

def binarySearch(key):
    list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    max = len(list)-1
    min = 0

    while (max > min):
        mid = list[(max+min)//2]
        if (key == mid):
            return mid
        elif (key < mid):
            max = len(list)//2
        else:
            min = len(list)//2
print(binarySearch(30))