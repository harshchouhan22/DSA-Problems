class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        return len(words[-1])

s= "   fly me   to   the moon  " 
result=  Solution().lengthOfLastWord(s)
print(result)

