
class Solution(object):
    def rotateString(self, s, goal):
        #First, Check if lengths are equal
        if len(s) != len(goal):
            return False
        
        #concatenate s with itself to create a string with all possible rotations
        s += s
        #Check of goal is a substring of the concatenated s
        print(s)
        return goal in s

s = "abcde"
goal = "cdeab"
result = Solution().rotateString(s, goal)
print(result)