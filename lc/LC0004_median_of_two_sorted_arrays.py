def findMedianSortedArrays(_, nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    if n1 > n2:
        nums1, nums2 = nums2, nums1

    (m, k), l1, r1 = divmod(n1 + n2 - 1, 2), 0, min(n1, n2)
    while l1 < r1:
        m1 = (l1 + r1) // 2
        m2 = m - 1 - m1
        if m2 < 0 or nums1[m1] > nums2[m2]:
            r1 = m1
        else:
            l1 = m1 + 1

    r2 = m - r1
    A = sorted(nums1[r1 : r1 + 2] + nums2[r2 : r2 + 2])
    return (A[0] + A[k]) / 2
