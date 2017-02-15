# coding: utf-8
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = [""]
        if len(s) == 1:
            return s

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                j = 0
                while j <= i and i + j <= len(s)-2:
                    if s[i-j] == s[i+1+j]:
                        tmp = s[i-j:i+2+j]
                        j += 1
                    else:
                        break
                ret.append(tmp)
            if i <= len(s)-3: 
                if s[i] == s[i+2]:
                    j = 0
                    while j <= i and i + j <= len(s)-3:
                        if s[i-j] == s[i+2+j]:
                            tmp = s[i-j: i+3+j]
                            j += 1
                        else:
                            break
                    ret.append(tmp)
        rr = s[0]
        for r in ret:
            if len(r) > len(rr):
                rr = r
        return rr