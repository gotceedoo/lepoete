def largestRectangleArea(self, heights): # sliding window w/ increasing mono-stack O(N)
    res = 0
    heights.append(0)                    # end at height 0 to ensure all heights processed later;
    asc = [-1]                           # stack will hold indices of increasing heights,
                                         # and begins w/ index of last height 0 to ensure itself non-empty,
                                         # thus avoid nullness check later.

    for j, r in enumerate(heights):      # r:   current right height
                                         # j:   index of current right height and wannabe current right of rectangle width,
                                         #      which is exclusive;
                                         # all indices will be pushed into stack and popped off exactly once, thus O(N).

        while heights[asc[-1]] > r:      # expand current window backward;
                                         # we will pop off indices of left heights greater than current right height,
                                         # calculate and maximize rectangle areas accordingly;

            l = heights[asc.pop()]       # l:   current rectangle height popped off, which is decreasing;
            i = asc[-1] + 1              # i:   current left of rectangle width, which is decreasing and inclusive;
            res = max(res, l * (j - i))  # res: running local maximum rectangle area,
                                         #      which is w/ decreasing height but increasing width in current window.

        asc.append(j)                    # move next window forward;
                                         # append index of current right height,
                                         # which is always greater than or equal to all remaining left heights.

    return res

