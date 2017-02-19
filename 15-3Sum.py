"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    
    def twoSum(self,s,target):
        i = 0
        j = len(s)-1
        r = []
        while i < j:
            a,b = s[i],s[j]
            if a + b == target:
                if [a,b] not in r:
                    r.append([a,b])
                i += 1
                j -= 1
            elif a + b < target:
                i += 1
            else:
                j -= 1
          
        return r
                
        
        
    def threeSum(self, num):
        
        ret = []
        pos = []
        neg = []
        zero = []
        
        for n in num:
            if n < 0:
                neg.append(n)
            elif n > 0:
                pos.append(n)
            else:
                zero.append(n)
        
        pos = sorted(pos)
        neg = sorted(neg)
        
        for p in set(pos):
            for a,b in self.twoSum(neg,-p):
                    ret.append([a,b,p])
            
        for n in set(neg):
            for a,b in self.twoSum(pos,-n):
                    ret.append([n,a,b])
            
        if len(zero) > 0:
            for a,b in self.twoSum(neg+pos,0):
                if [a,0,b] not in ret:
                    ret.append([a,0,b])
            if len(zero) >= 3:
                ret.append([0,0,0])
                
        return ret
