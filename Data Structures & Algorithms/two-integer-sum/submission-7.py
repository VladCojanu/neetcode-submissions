class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # linear pass w/ hashmap
        seen = {}

        for i in range(len(nums)):
            j_val = target - nums[i]
            if j_val in seen:
                return sorted([i, seen[j_val]])
            else: 
                seen[nums[i]] = i
        raise Exception('un-expected - we expect to arrive at a solution')