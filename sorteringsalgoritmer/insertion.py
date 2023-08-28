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
arr = [2, 3, 6, 5, 4]
print(insertion(arr))