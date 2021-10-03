def findMedianSortedArrays(_, nums1, nums2):  # solution 1
    l1, r1, n2 = 0, len(nums1), len(nums2)
    m, k = divmod(r1 + n2 - 1, 2)

    while l1 < r1:
        m1 = (l1 + r1) // 2
        m2 = m - m1 - 1
        if m2 < 0 or m2 < n2 and nums1[m1] > nums2[m2]:
            r1 = m1
        else:
            l1 = m1 + 1

    r2 = m - r1
    A = sorted(nums1[r1 : r1 + 2] + nums2[r2 : r2 + 2])
    return (A[0] + A[k]) / 2


def findMedianSortedArrays(_, nums1, nums2):  # solution 2
    n1, n2 = len(nums1), len(nums2)
    m, k = divmod(n1 + n2 - 1, 2)

    class wrap:
        def __getitem__(_, m1):
            m2 = m - m1 - 1
            return m2 < 0 or m2 < n2 and nums1[m1] > nums2[m2]
    r1 = bisect.bisect(wrap(), False, 0, n1)

    r2 = m - r1
    A = sorted(nums1[r1 : r1 + 2] + nums2[r2 : r2 + 2])
    return (A[0] + A[k]) / 2
