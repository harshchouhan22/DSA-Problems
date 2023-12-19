class Solution(object):
    def plusOne(self, digits): 
        value = ''.join(map(str, digits))
        int(value)
        value = int(value) + 1
        result_list = []
        for i in str(value):
            result_list.append(int(i))
        return result_list
        
        

digits = [9, 8]
result = Solution().plusOne(digits)
print(result)