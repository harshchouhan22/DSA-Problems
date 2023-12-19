class Solution(object):
    def isGood(self, nums):
        n = max(nums)
        base_n = list(range(1, n)) + [n, n]
        print(base_n)
        return sorted(nums) == sorted(base_n)


nums = [1, 3, 3, 2]
result =  Solution().isGood(nums)
print(result)
