class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped_dict = {}
        for strings in strs:
            sorted_value = "".join(sorted(strings))
            if sorted_value in mapped_dict:
                mapped_dict[sorted_value].append(strings)
            else:
                mapped_dict[sorted_value] = [strings]

        ans = []
        for key, value in mapped_dict.items():
            ans.append(value)

        return ans
