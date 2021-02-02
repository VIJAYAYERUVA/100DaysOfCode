# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
def twosum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i


query = twosum(nums=[3, 4, 2], target=6)
print(query)
