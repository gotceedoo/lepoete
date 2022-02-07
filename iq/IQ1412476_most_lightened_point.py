def most_lightened_point(lamps):
    points = collections.defaultdict(int)
    for x, r in lamps:
        points[x - r] += 1
        points[x + r + 1] -= 1
    points = dict(sorted(points.items()))
    points = dict(zip(points.keys(), itertools.accumulate(points.values())))
    return max(points, key=points.get)
