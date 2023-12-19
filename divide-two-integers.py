
class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        #Handle edge case of the division by zero
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN
        
        #Handle overflow cases
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        #Determine the sign of thr result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        #Take the absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)

        #Initialize the quotient
        quotient = 0

        #Bitwise  the quotient
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple
        return sign * quotient
    




dividend = 10
divisor = 4
result = Solution().divide(dividend, divisor)
print(result)
