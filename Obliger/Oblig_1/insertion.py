import sys, time

def insertion(arr):
    for i in range(len(arr)):   # iterate over array linear
        key = arr[i]               # key always is current value of index
        j = i - 1                  # j is always (i-1)

        while j >= 0 and key < arr[j]:   # while (j>0 == not at first index) and (key < (arr[i-1] == arr[j]))
            arr[j+1] = arr[j]           # current index value equals (current index-1 value == j)
            j -= 1                      # j is decremented and while loop continues to the next element

        # the current empty space which is j+1 is set to key. key might already be there if no changes in while-loop
        arr[j+1] = key
    return arr

# ((n-1)*n)/2   ->  (n)*n   ->  O(n^2)


# sort from argument input:
arr = []
with open(sys.argv[1]) as f:
    for n in f:
        arr.append(int(n.strip()))
        insertion(arr)

# write to new file:
nf = open(sys.argv[1].split(".")[0] + "_insertion.out.csv", "w")
for n in [str(n) for n in arr]:
    nf.write(n + "\n")