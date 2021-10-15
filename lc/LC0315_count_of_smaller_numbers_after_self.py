def countSmaller(self, nums):
    n, size = 1, len(nums)
    A, dp = list(range(size)), [0] * size
    while n < size:
        for i in range(0, size, n * 2):
            L, R = A[i : i + n], A[i + n : i + n * 2]
            for j in range(i, i + len(L) + len(R))[::-1]:
                if not R or L and nums[L[-1]] > nums[R[-1]]:
                    dp[L[-1]] += len(R)
                    A[j] = L.pop()
                else:
                    A[j] = R.pop()
        n *= 2
    return dp
