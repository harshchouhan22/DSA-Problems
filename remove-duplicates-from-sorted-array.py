class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1 #Initialize k to 1 since the first element is always unique
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1 # k = k +1
        return k

nums = [1, 1, 2]
k = Solution().removeDuplicates(nums)
print(k)
