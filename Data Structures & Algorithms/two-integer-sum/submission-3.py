class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # assumptions: 
        # 1. always an answer
        # 2. smaller index first

        i = 0 
        j = 1 
        while i < len(nums) and j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            
            if j + 1 == len(nums): 
                i += 1
                j = i + 1 
            else: 
                j += 1
        # not possible to reach here based on problem statemnet 
        raise Error('invalid nums array for target')


# Test Cases

#  [1,2,3,4] target = 5
# 

#  Runtime

# O(n^2)