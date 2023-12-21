
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #Start form the end of both arrays
        i, j, k = m - 1, n - 1, m + n - 1

        #Iterate over arrays from the end
        while i >= 0 and j >=0 :
            #compare elements at nums1[i] and nums2[j]
            if nums1[i] > nums2[j]:
                #Copy nums1[i] to the last poisition in the merged array
                nums1[k] = nums1[i]
                i -= 1
            else:
                #Copy nums2[j] to the last poisition in the merged array
                nums1[k] = nums2[j]
                j -= 1
            #Move to the previous position in the merged array
            k -= 1
        #If there are remaining elements in nums2, copy them to the merged array
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
num1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
result = Solution().merge(num1, m, nums2, n)
print(result)