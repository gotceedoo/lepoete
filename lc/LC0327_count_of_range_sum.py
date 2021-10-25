def countRangeSum(self, nums, lower, upper):
    A = list(itertools.accumulate(nums, initial=0))             # prepare the array of prefix sums
    size, res = len(A), 0

    for n in range(math.ceil(math.log(size, 2))):               # iterate to mergesort logN times

        n = 2 ** n                                              # set size of half partition
        for l in range(0, size, 2 * n):                         # iterate over partitions

            i = j = m = l + n                                   # set beginning of two pointers, i.e. middle of partition
            r = min(m + n, size)                                # set end of two pointers, i.e. right of partition
            for k in range(l, m):                               # iterate over left half
                while i < r and A[i] - A[k] <  lower: i += 1    # step forward till lower boundary satisfied over right half
                while j < r and A[j] - A[k] <= upper: j += 1    # step forward till upper boundary unsatified over right half
                res += j - i                                    # add up count of range sum satisfied beginning w/ kth element over left half

            L, R = A[l:m], A[m:r]                               # prepare left and right halves
            for i in range(l, r)[::-1]:                         # execute mergesort per partition
                if not R or L and L[-1] > R[-1]: A[i] = L.pop()
                else:                            A[i] = R.pop()

    return res
