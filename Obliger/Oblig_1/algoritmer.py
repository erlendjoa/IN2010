import sys, time

def addCMP(algorithmArr):
    algorithmArr[0] += 1
def addSWAP(algorithmArr):
    algorithmArr[1] += 1

def insertion(arr):
    for i in range(len(arr)):   # iterate over array linear
        key = arr[i]               # key always is current value of index
        addCMP(insertionOutArr)

        j = i - 1                  # j is always (i-1)
        addCMP(insertionOutArr)

        while j >= 0 and key < arr[j]:   # while (j>0 == not at first index) and (key < (arr[i-1] == arr[j]))
            arr[j+1] = arr[j]           # current index value equals (current index-1 value == j)
            addCMP(insertionOutArr)
            addSWAP(insertionOutArr)
            
            j -= 1                      # j is decremented and while loop continues to the next element
            addCMP(insertionOutArr)
            

        # the current empty space which is j+1 is set to key. key might already be there if no changes in while-loop
        arr[j+1] = key
        addCMP(insertionOutArr)
            
    return arr


def mergeSort(arr):
    addCMP(mergeOutArr)
    if len(arr) <= 1:   # return smallest length array of len() 1
        return arr

    
    middle = len(arr)//2    # find the middle of array
    addCMP(mergeOutArr)

    leftArr = mergeSort(arr[:middle])   # sorted left array, sorts all the way to a len() of 1
    rightArr = mergeSort(arr[middle:])  # sorted right array
    addCMP(mergeOutArr)
    addCMP(mergeOutArr)

    # return the merged two arrays. Arguments are current left and right arr of current overhead array (arr)
    return merge(leftArr, rightArr, arr)

def merge(arrA, arrB, arr):
    i = 0
    j = 0
    addCMP(mergeOutArr)
    addCMP(mergeOutArr)

    # check which element is smallest and insert/overwrite at arr[i+j]. Increment i or j after
    while i < len(arrA) and j < len(arrB):
        addCMP(mergeOutArr)
        if arrA[i] <= arrB[j]:
            arr[i+j] = arrA[i]
            i += 1
            addCMP(mergeOutArr)
            addCMP(mergeOutArr)
            addSWAP(mergeOutArr)
        else:
            arr[i+j] = arrB[j]
            j += 1
            addCMP(mergeOutArr)
            addCMP(mergeOutArr)

    # insert rest of the array while either i or j == len(arrA/B)
    while i < len(arrA):
        arr[i+j] = arrA[i]
        i += 1
        addCMP(mergeOutArr)
        addCMP(mergeOutArr)
        addSWAP(mergeOutArr)
    while j < len(arrB):
        arr[i+j] = arrB[j]
        j += 1
        addCMP(mergeOutArr)
        addCMP(mergeOutArr)

    return arr  # return sorted array


def writeToFile():
    nf = open(sys.argv[1].split(".")[0] + "_results.csv", "a")

    nf.write(str(nrOfN))

    for n in [str(n) for n in insertionOutArr]:
        nf.write(", " + n)
    for n in [str(n) for n in mergeOutArr]:
        nf.write(", " + n)
    nf.write("\n")

# declare global variables:
insertionArr = []
mergeArr = []
nrOfN = 0
    
# empty file:
nf = open(sys.argv[1].split(".")[0] + "_results.csv", "w")

# sort from argument input:
with open(sys.argv[1]) as f:
    for n in f:

        insertionOutArr = [0, 0, 0]
        mergeOutArr = [0, 0, 0]

        # run once empty:
        insertion(insertionArr)
        mergeSort(mergeArr)

        nrOfN += 1  # add 1 to number of total N
        insertionArr.append(int(n.strip()))
        mergeArr.append(int(n.strip()))

        t = time.time()*1000.0 # start timer
        insertion(insertionArr)
        insertionOutArr[2] = (time.time_ns() - t) / 1000 # finish up timer

        t = time.time()*1000.0 # start timer
        mergeSort(mergeArr)
        mergeOutArr[2] = (time.time_ns() - t) / 1000 # finish up timer

        writeToFile()