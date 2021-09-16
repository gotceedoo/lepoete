"""

We can observe the patterns on this problem as follows,

+ Numbers of base 10 are translated into combo of base 10 and 26.
  - Most significant part is base 26 on the right while base 10 on the left.
  - Most significant place of either base 10 or 26 is on the left.
+ Numbers under translation fall into one of 6 successive sub-ranges in line with place distribution between base 10 and 26.
  - ["00000", "99999"] for [      0,    99999], i.e.      -1+10^5*26^0
  - ["0000A", "9999Z"] for [ 100000,   359999], i.e    99999+10^4*26^1
  - ["000AA", "999ZZ"] for [ 360000,  1035999], i.e.  359999+10^3*26^2
  - ["00AAA", "99ZZZ"] for [1036000,  2793599], i.e. 1035999+10^2*26^3
  - ["0AAAA", "9ZZZZ"] for [2793600,  7363359], i.e. 2793599+10^1*26^4
  - ["AAAAA", "ZZZZZ"] for [7363360, 19244735], i.e. 7363359+10^0*26^5

We reversely iterate over the sub-ranges to match one of them.
To conclude the translation we then step over the parts as well as the places from least to most significant one.

"""


def find_nth_license_plate(n):
    ranges = [0] * 6
    for place in range(5):
        ranges[place + 1] = ranges[place] + 10 ** (5 - place) * 26 ** place

    parts = [""] * 2
    for place, low in enumerate(ranges[::-1]):
        if n < low: continue
        n -= low
        for i, (part, base, first) in enumerate([(place, 10, "0"), (5 - place, 26, "A")]):
            for _ in range(part):
                n, k = divmod(n, base)
                parts[i] = chr(k + ord(first)) + parts[i]
        return "".join(parts)
