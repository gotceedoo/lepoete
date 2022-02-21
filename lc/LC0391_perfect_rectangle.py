def isRectangleCover(self, rectangles):
    cnt = collections.defaultdict(int)
    for x, y, a, b in rectangles:
        cnt[x, y] += 1
        cnt[x, b] -= 1
        cnt[a, b] += 1
        cnt[a, y] -= 1
    return sum(map(abs, cnt.values())) == 4
