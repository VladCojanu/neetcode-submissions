class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


    # linear loop O(n)
    # loop-up log(n) or O(1) -> in python O(1)
