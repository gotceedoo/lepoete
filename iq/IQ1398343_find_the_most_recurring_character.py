"""

Two patterns are observed on this problem below,
- every character position is reachable from previous (2^i-1)th positions, thus log(n)+1 in total;
- every character position is periodic in length 26.

Let's draw the char array to illustrate the points.

char array:                    ............................................................................
number of segments:            |  1 | 2 | 3 | 4 |  5       |  6      |  7             |   8            |...
length of 2^i per segment:     |  1 | 2 | 4 | 8 | 16       | 32      | 64             | 128            |...
number of periods:             |  1                  |  2       |  3      |    4 |  5       |    9 |.......
length of 26 per period:       | 26                  | 26       | 26      | 26*1 | 26       | 26*4 |.......
parts per segment:             | n/a                 |  r |  l  |  r |  l |    m |  r |   l |    m | 8 |...
number of reachables per part: | n/a                 |  5 |  6  |  6 |  7 |  7*1 |  7 |   8 |  8*4 | 8 |...

To conclude the counting, we iterate over those segments of k=log(n)+1 and sum the reachables per part.

"""


def find_the_most_recurring_character(n):                          # Math pattern O(26*logN)

                                                                   # Note on this problem:
                                                                   # - power (**) can be replaced by right shift (<<).
                                                                   # - int(math.log) can be replace by the customized one:
                                                                   #   lg2 = lambda n: n > 1 and lg2(n >> 1) + 1

    cnt = [int(math.log(j + 1, 2)) + 1 for j in range(min(n, 26))] # count against length no more than 26.

    k = int(math.log(n, 2)) + 1                                    # number of segments,
    for i in range(1, k + 1):                                      # iterate over segments to sum up reachables per part;

        l = 2 ** (i - 1)                                           # length against left part,
        for j in range(l % 26 - 1, i >= 6 and 26):                 # add left part from 6th segment onward;
            cnt[j] += i

        m = min(n, 2 ** i)                                         # length against middle part,
        for j in range(i >= 7 and 26):                             # add middle part from 7th segment onward;
            cnt[j] += i * (m // 26 - l // 26 - 1)

        r = min(n, 2 ** i - 1)                                     # length against right part,
        for j in range(r >= 27 and r % 26):                        # add right part from 27th position onward.
            cnt[j] += i

    return max(cnt), "".join(chr(j + ord("A")) for j, n in enumerate(cnt) if n == max(cnt))
