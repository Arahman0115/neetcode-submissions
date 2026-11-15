from heapq import heappush,heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            freq_dict[i] = freq_dict.get(i, 0) + 1
        heap = []
        print(freq_dict)
        for num, freq in freq_dict.items():
            if len(heap) == k:
                heappushpop(heap,[freq_dict[num],num])
            else:
                heappush(heap,[freq_dict[num],num])
        res = [num for freq,num in heap]
        return res