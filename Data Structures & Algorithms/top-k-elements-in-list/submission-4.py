from heapq import heappush, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            freq_dict[i] = freq_dict.get(i,0) + 1
        print(freq_dict)
        heap = []
        for num, freq in freq_dict.items():
            if len(heap) == k:
                heappushpop(heap,[freq,num])
            else:
                heappush(heap,[freq,num])
        res = [num for freq,num in heap]
        return res