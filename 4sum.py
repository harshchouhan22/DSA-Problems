class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            #skip the duplicate i
            if i > 0 and i == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                #skip duplicate for j
                if j > i + 1 and nums[j] == nums[i - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result

nums = [2, 2, 2, 2, 2]
target = 8
result = Solution().fourSum(nums, target)
print(result)
