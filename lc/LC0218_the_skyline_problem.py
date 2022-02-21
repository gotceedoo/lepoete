def getSkyline(self, buildings): # O(NlogN)
    res, q, intervals = [[None, 0]], [(0, math.inf)], []
    for l, r, h in buildings:
        intervals += (l, -h, r), (r, 0, None)
    for x, y, r in sorted(intervals):
        while x >= q[0][1]:
            heapq.heappop(q)
        if y:
            heapq.heappush(q, (y, r))
        if res[-1][1] + q[0][0]:
            res += [x, -q[0][0]],
    return res[1:]
