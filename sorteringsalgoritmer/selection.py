def selection(arr):
    for i in range(len(arr)):   # iterate over array linear
        min = i                 # min is set to the index of current smalles number
        
        for j in range(i, len(arr)-1):  # iterate from i to end of array
            if (arr[j] < arr[min]):          # if "current" spot of j is smaller than "current" spot of min, set it to be min
                min = j
        
        # swap the places of current index selected and min (the index for smallest number)
        arr[i], arr[min] = arr[min], arr[i]
    return arr

#ex:
arr = [2, 3, 6, 5, 4]
print(selection(arr))

# (n-1)*(n-2-3-4--5)/2  ->  (n)*n/2 ->  O(n^2)