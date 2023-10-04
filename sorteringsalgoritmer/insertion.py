def insertion(arr):
    for i in range(1, len(arr)):   # iterate over array linear
        key = arr[i]               # key always is current value of index
        j = i - 1                  # j is always (i-1)

        while j > 0 and key < arr[j]:   # while (j>0 == not at first index) and (key < (arr[i-1] == arr[j]))
            arr[j+1] = arr[j]           # current index value equals (current index-1 value == j)
            j -= 1                      # j is decremented and while loop continues to the next element

        # the current empty space which is j+1 is set to key. key might already be there if no changes in while-loop
        arr[j+1] = key
    return arr

#ex:
arr = [0,1,7,2,4,11,10,5,12,6,9,29,14,28,21]
print(insertion(arr))

# ((n-1)*n)/2   ->  (n)*n   ->  O(n^2)