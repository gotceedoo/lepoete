def countRangeSum(self, nums, lower, upper):
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
                while k < r and R[k] < x: # handcraft mergesort
                    A[l] = R[k]
                    l += 1
                    k += 1
                A[l] = x
                l += 1
        n *= 2
    return res
