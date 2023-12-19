class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        sum_int = a + b
        result = bin(sum_int)[2:]
        return result
a='11'
b='1'
result = Solution().addBinary(a, b)
print(result)
