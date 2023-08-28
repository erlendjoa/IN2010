def bubble(arr):
    for i in range(len(arr)-1):             # iterate linear
        for j in range(0, len(arr)-i-1):    # iterate from start to (end-i-1) excluding the rest and 1 because of indexOutOfBounds
            if (arr[j] > arr[j+1]):             
                # swap the two adjacent, end up with the smallest on index i and biggest on index len(arr)-i-1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#ex:
arr = [2, 3, 6, 5, 4]
print(bubble(arr))

# (n-1)*n/2 ->  O(n^2)