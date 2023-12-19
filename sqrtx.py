class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x
        result = 0
        while left <= right:
            mid = (left + right) // 2
            print('left ', left, 'right',)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                print('mid mul',( mid * mid))
                left = mid + 1
                result = mid
            else:
                right = mid - 1
        return result
x = 8
result = Solution().mySqrt(x)
print(result)
