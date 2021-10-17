def countSmaller(self, nums):
    size = len(nums)
    A, dp = list(range(size)), [0] * size
    for n in range(math.ceil(math.log(size, 2))):                       # iterate to mergesort logN times
        for i in range(0, size, 2 ** (n + 1)):                          # iterate over partitions
            L, R = A[i : i + 2 ** n], A[i + 2 ** n : i + 2 ** (n + 1)]  # prepare left and right parts per partition
            for j in range(i, i + len(L) + len(R))[::-1]:               # iterate over elements per partition and execute mergesort
                if not R or L and nums[L[-1]] > nums[R[-1]]:
                    dp[L[-1]] += len(R)                                 # add up count of smallers per element
                    A[j] = L.pop()
                else:
                    A[j] = R.pop()
    return dp
