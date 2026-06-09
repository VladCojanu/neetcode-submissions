from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)        
        for n in nums:
            seen[n] += 1
        heap = []
        for num, freq in seen.items():
            heapq.heappush(heap, (freq, num))
        while len(heap) > k:
            heapq.heappop(heap)

        return [v[1] for v in heap]
        
# n = len(nums)
# m unique nums
# Space O(m)
# Time O(n+mlogm)

'''
I need some strucutre where I can store the more seen values 
'''