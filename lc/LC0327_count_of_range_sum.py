def countRangeSum(self, nums, lower, upper):
    A = list(itertools.accumulate(nums, initial=0))             # prepare the array of prefix sums
    size, res = len(A), 0

    for n in range(math.ceil(math.log(size, 2))):               # iterate to mergesort logN times

        for l in range(0, size, 2 ** (n + 1)):                  # iterate over partitions

            i = j = l + 2 ** n                                  # locate the start of two pointers, i.e. the middle per partition
            r = min(l + 2 ** (n + 1), size)                     # locate the end of two pointers, i.e. the right per partition
            L, R = A[l:i], A[i:r]                               # prepare left and right parts per partition

            for x in L:                                         # iterate over left part per partition
                while i < r and A[i] - x <  lower: i += 1       # step forward till lower boundary satisfied over right part per partition
                while j < r and A[j] - x <= upper: j += 1       # step forward till upper boundary unsatified over right part per partition
                res += j - i                                    # add up count of range sum satisfied per element

            for i in range(l, r)[::-1]:                         # execute mergesort per partition
                if not R or L and L[-1] > R[-1]: A[i] = L.pop()
                else:                            A[i] = R.pop()
    return res
