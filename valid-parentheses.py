

class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in bracket_dict.values():
                stack.append(char)
            elif char in bracket_dict.keys():
                if not stack or stack.pop() != bracket_dict[char]:
                    return False
        return not stack
             
string = "()[]{}"
result = Solution().isValid(string)
print(result)
