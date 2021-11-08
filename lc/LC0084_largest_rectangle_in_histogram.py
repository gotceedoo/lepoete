def largestRectangleArea(self, heights):
    res, A, H = 0, [], [0] + heights + [0]
    for i, h in enumerate(H):
        while A and H[A[-1]] > r:
            res = max(res, A.pop() * (i - 1 - A[-1]))
        A.append(i)
    return res
