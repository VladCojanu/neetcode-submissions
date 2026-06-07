class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for c in s:
            if c in letters: 
                letters[c] = letters[c] + 1
            else:
                letters[c] = 1
        
        for c in t:
            if c not in letters:
                return False
            count = letters[c]
            if count > 0:
                letters[c] = letters[c] - 1
            else: 
                return False

        return True


#  Test cases

'''
s = 'a', t = 'bc' -> early exit False.
s = 'ab' t = 'aa' -> True, but actually False. 
s = abc t  = cba

letters = {a => 0, b => 1}

s = 'aabb' t = 'aaab' -> True, but actually False

'''


# Run Time

#  O(n)
# Space O(n)