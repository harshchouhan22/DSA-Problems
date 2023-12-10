
class Solution():
    def reverse_integer(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        str_x = str(x)
        sign = 1 if x >= 0 else -1
        reversed_x = int(str_x[::-1]) * sign
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
        return reversed_x

x = 123
result = Solution().reverse_integer(x)
print(result)
