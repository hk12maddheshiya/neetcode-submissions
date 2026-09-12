class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for c, i in enumerate(nums):
            s.add(i)
            if len(s) != c+1 :
                return True

        return False