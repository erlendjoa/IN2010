class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]

    def swap_merge(self, i, j, other):
        self[i], other[j] = other[j], self[i]

    def increment_swap(self, arrA, arrB):
        self.swaps += (arrA.swaps + arrB.swaps)