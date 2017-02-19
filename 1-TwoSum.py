"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n = sorted(num)
        
        i = 0
        j = len(n) - 1
        a,b = 0,0
        while(j > i):
            if n[i] + n[j] == target:
                a,b = n[i], n[j]
                break
            elif n[i] + n[j] < target:
                i = i+1
            else:
                j = j-1
                
        p,q = num.index(a), num.index(b)
        if p > q:
            p,q = q,p
            
        elif p == q:
            num.remove(a)
            q = num.index(b) + 1
            
        return (p+1,q+1)
