import sys, time

t = time.time_ns()  # start timer

def mergeSort(arr):
    if len(arr) <= 1:   # return smallest length array of len() 1
        return arr
    
    middle = len(arr)//2    # find the middle of array

    leftArr = mergeSort(arr[:middle])   # sorted left array, sorts all the way to a len() of 1
    rightArr = mergeSort(arr[middle:])  # sorted right array

    # return the merged two arrays. Arguments are current left and right arr of current overhead array (arr)
    return merge(leftArr, rightArr, arr)


def merge(arrA, arrB, arr):
    i = 0
    j = 0

    # check which element is smallest and insert/overwrite at arr[i+j]. Increment i or j after
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            arr[i+j] = arrA[i]
            i += 1
        else:
            arr[i+j] = arrB[j]
            j += 1

    # insert rest of the array while either i or j == len(arrA/B)
    while i < len(arrA):
        arr[i+j] = arrA[i]
        i += 1
    while j < len(arrB):
        arr[i+j] = arrB[j]
        j += 1

    return arr  # return sorted array

# merge: O(n), mergeSort: log(n)    ->  O(n*log(n))

arr = []
# sort from argument input:
with open(sys.argv[1]) as f:
    for n in f:
        arr.append(int(n.strip()))
        mergeSort(arr)

# finish up timer
timeus = (time.time_ns() - t) / 1000

# write to new file:
nf = open(sys.argv[1].split(".")[0] + "_merge.out.csv", "w")
for n in [str(n) for n in arr]:
    nf.write(n + "\n")