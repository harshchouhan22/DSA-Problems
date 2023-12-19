
class Solution(object):
    def strStr(self, haystack, needle):
        try:
            return haystack.find(needle)
        except:
            return -1

haystack = "sadbutsad"
needle = "sad"
result = Solution().strStr(haystack, needle)
print(result)