
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        n = len(nums)
        threshold = n // 3 
        counter = Counter(nums)
        result = set() #Use a set to store unique elements that meet the conditions

        for num, count in counter.items():
            if count > threshold:
                result.add(num) #add elements to the results
        return list(result)
nums = [3, 2, 3]
result = Solution().majorityElement(nums)
print(result)
