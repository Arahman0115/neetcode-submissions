from heapq import heappush, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            freq_dict[i] = freq_dict.get(i,0) + 1
        heap = []
        for key in freq_dict.keys():
            if len(heap) == k:
                heappushpop(heap,[freq_dict[key],key])
            else:
                heappush(heap,[freq_dict[key],key])
        res = [num for freq,num in heap]
        return res 
