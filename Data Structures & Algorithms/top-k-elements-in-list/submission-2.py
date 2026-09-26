from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count each number's frequency
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # buckets[frequency] contains numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        # Collect from highest frequency to lowest
        result = []

        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

        return result