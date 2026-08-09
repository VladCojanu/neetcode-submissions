class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanatized = "".join(c for c in s if c.isalnum())

        h_len = len(sanatized) // 2

        for i in range(h_len):
            if sanatized[i].lower() != sanatized[-1-i].lower():
                return False
        return True 
