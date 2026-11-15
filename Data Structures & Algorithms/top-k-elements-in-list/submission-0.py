import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        sorted_by_values = dict(sorted(frequency_dict.items(), key=lambda item: item[1]))
        last_two_keys = list(sorted_by_values.keys())[-k:]
        return last_two_keys