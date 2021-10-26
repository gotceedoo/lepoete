def countRangeSum(self, nums, lower, upper):                 # solution 1: builtin mergesort
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


def countRangeSum(self, nums, lower, upper):                 # solution 2: handmade mergesort
    N, n, res = len(nums) + 1, 1, 0
    A = list(itertools.accumulate(nums, initial=0))
    while n < N:
        for l in range(0, N, n * 2):
            m = l + n
            L, R = A[l:m], A[m : m + n]
            r = len(R)
            i = j = k = 0
            for x in L:
                while i < r and R[i] - x <  lower: i += 1
                while j < r and R[j] - x <= upper: j += 1
                res += j - i
                while k < r and R[k] < x:
                    A[l] = R[k]
                    l += 1
                    k += 1
                A[l] = x
                l += 1
        n *= 2
    return res
