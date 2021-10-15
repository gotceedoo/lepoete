def countSmaller(self, nums):
    def sort(ids):
        half = len(ids) // 2
        if half:
            L, R = sort(ids[:half]), sort(ids[half:])
            for i in range(len(ids))[::-1]:
                if not R or L and nums[L[-1]] > nums[R[-1]]:
                    cnts[L[-1]] += len(R)
                    ids[i] = L.pop()
                else:
                    ids[i] = R.pop()
        return ids

    cnts = [0] * len(nums)
    sort(list(range(len(nums))))
    return cnts


def countSmaller(self, nums):
    n, size = 1, len(nums)
    ids, cnts = list(range(size)), [0] * size
    while n < size:
        for i in range(0, size, n * 2):
            L, R = ids[i : i + n], ids[i + n : i + n * 2]
            for j in range(i, i + len(L) + len(R))[::-1]:
                if not R or L and nums[L[-1]] > nums[R[-1]]:
                    cnts[L[-1]] += len(R)
                    ids[j] = L.pop()
                else:
                    ids[j] = R.pop()
        n *= 2
    return cnts
