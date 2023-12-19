
class Solution(object):
    def removeElement(self, nums, val):
        #Use list comprehension to create a new list without
        nums[:] =  [num for num in nums if num != val]
        return len(nums)

val = 2
nums = [3,2,2,3]

result = Solution().removeElement(nums, val)
print(result)
