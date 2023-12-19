class Solution(object):
    def generateParenthesis(self, n):
        def generate(partial, left, right):
            if left == 0 and right == 0:
                result.append(partial)
                return
            if left > 0:
                generate(partial + '(', left - 1, right)
            if right > left:
                generate(partial + ')', left, right - 1)
        result = []
        generate('', n, n)
        return result

n1 = 3
n2 = 1

output1 = Solution().generateParenthesis(n1)  # Corrected method name
output2 = Solution().generateParenthesis(n2)  # Corrected method name

print("Input: n =", n1)
print("Output:", output1)

print("\nInput: n =", n2)
print("Output:", output2)
