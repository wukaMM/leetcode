"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ret  = 0
        i = 0
        j = 0
        while i<len(s):
            while j<len(s):
                if s[j] not in s[i:j]:
                    j += 1
                    if j == len(s):
                        ret = max(ret, j-i)
                else:
                    ret = max(ret, j-i)
                    while s[i] != s[j]:
                        i += 1
                    i += 1
                    break
            if j == len(s):
                break

        return ret

#####################
THE BETTER SOLUTION
#####################

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        l  = 0
        d = {}
        m = 0
        
        for r,c in enumerate(s):
            t = d.get(c,None)
            if t is not None and t >= l:
                l = t + 1
            
            d[c] = r
            m = max(m,r-l+1)

        return m
