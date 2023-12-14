class Solution(object):
    def romanToInt(self, s):
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0

        for i in s:
            for key, value in dic.items():
                if i == key:
                    if prev_value < value:
                        result += value - 2 * prev_value
                    else:
                        result += value
                    prev_value = value

        return result

string = "MCMXCIV"
result = Solution().romanToInt(string)
print(result)
