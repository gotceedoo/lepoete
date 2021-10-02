def gcdSort(self, nums):
    def find(n):
        if uf[n] != n:
            uf[n] = find(uf[n])  # path compression
        return uf[n]

    uf, vis, seen = list(range(100001)), [False] * 100001, set(nums)
    for i in range(
        2, 100001
    ):  # iterate over successive natual numbers beginning with 2
        if vis[i]:
            continue  # skip visited including any composite number
        for j in range(i, 100001, i):  # iterate over the prime and its multiples
            vis[j] = True  # mark them visited
            if j in seen:
                uf[find(j)] = find(
                    i
                )  # union connected numbers containing same prime factor

    return all(
        find(x) == find(y) for x, y in zip(nums, sorted(nums))
    )  # swappable if each of pair numbers connected
