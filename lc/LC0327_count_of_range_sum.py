def countRangeSum(self, nums, lower, upper):
    res, size = 0, len(nums) + 1
    A = list(itertools.accumulate(nums, initial=0))          # prepare array of prefix sums
    for n in range(math.ceil(math.log(size, 2))):            # iterate to mergesort: O(logN)
        n = 2 ** n                                           # set size of half partition
        for l in range(0, size, 2 * n):                      # iterate over partitions: O(N) together w/ inner iterations
            i = j = l + n                                    # set beginning of two pointers to that of right half
            r = min(i + n, size)                             # set end of two pointers to that of right half
            for k in range(l, i):                            # iterate over left half
                while i < r and A[i] - A[k] <  lower: i += 1 # step forward till lower satisfied over right half
                while j < r and A[j] - A[k] <= upper: j += 1 # step forward till upper unsatified over right half
                res += j - i                                 # add up count of range sum satisfied beginning w/ kth element over left half
            A[l:r] = sorted(A[l:r])                          # builtin timsort, variation of mergesort
    return res
