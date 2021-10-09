def count_partitions_of_equal_sum(nums):
    count, total = 0, sum(nums)
    prefix = collections.Counter(list(itertools.accumulate(nums))[:-1])
    suffix = collections.Counter(list(itertools.accumulate(nums[::-1]))[:-1])
    for num in nums:
        changed, skip = divmod(total - num, 2)
        if skip: continue
        unchanged = changed + num
        this = prefix[changed] and suffix[unchanged]
        that = num and suffix[changed] and prefix[unchanged]
        count = max(count, this + that)
    return count
