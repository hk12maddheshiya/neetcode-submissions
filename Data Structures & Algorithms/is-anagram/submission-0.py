class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        for index , ch in enumerate(s):
            if t[index] != ch:
                return False

        return True