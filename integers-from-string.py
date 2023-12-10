

class Solution(object):
    def myAtoi(self, s):
        input_string = s
        result = 0
        for char in input_string:
            print(char)
            if char.isdigit():
                result = char
                print(char)
                return result




# Example usage:
input_str = " sHsugi698608"
result = Solution().myAtoi(input_str)
print(result)


