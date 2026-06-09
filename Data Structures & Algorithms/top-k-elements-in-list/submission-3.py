from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)        
        for n in nums:
            seen[n] += 1
        
        sorted_seen = list(dict(sorted(seen.items(), key=lambda i: i[1])).keys())

        
        return sorted_seen[len(sorted_seen)-k:]

'''
I need some strucutre where I can store the more seen values 
'''