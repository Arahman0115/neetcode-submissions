from heapq import heappushpop
from heapq import heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        
        heap = []

        for num in freq_dict.keys():
            if len(heap) == k:
                heappushpop(heap,[freq_dict[num],num])
            else:
                heappush(heap,[freq_dict[num],num])
        res = [num for freq,num in heap]
        return res