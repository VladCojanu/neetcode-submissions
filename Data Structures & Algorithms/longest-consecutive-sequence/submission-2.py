class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        num_set = set(nums)
        
        curr_len = 0 
        longest_len = 0 
        

        for i in nums:
            if i - 1 in num_set:
                continue 
            # compute length 
            curr_len = 1 
            n = i 
            while n + 1 in num_set:
                curr_len += 1
                n += 1

            longest_len = max(curr_len, longest_len)

        return longest_len