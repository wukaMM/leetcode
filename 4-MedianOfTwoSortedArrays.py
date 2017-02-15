# coding: utf-8

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

2个排好序的数组，m, n
取中间的值 m = [1,2], n = [3,4] ==> 2.5, m = [1], n = [2,3] ==> 2

思路：k 为前面需要舍弃的个数，每次尽量舍弃 k//2 个, 时间复杂度为 log((m+n)/2), 因为 k = (m+n)/2

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = nums1
        n = nums2
        c = len(m)+len(n)
        if c % 2 == 0:
            k = c//2 -1
        else:
            k = c//2

        while k > 0 and len(m) > 0 and len(n) > 0:
            if k == 1:
                if m[0] < n[0]:
                    m = m[1:]
                else:
                    n = n[1:]
                k = 0
                break
            _k = k//2
            if len(m) >= _k and len(n) >= _k:
                if m[_k-1] > n[_k-1]:
                    n = n[_k: ]
                    k = k - _k

                elif m[_k-1] <= n[_k-1]:
                    m = m[_k: ]
                    k = k - _k

            elif len(m) < _k and len(n) > _k:
                if m[-1] > n[_k-1]:
                    n = n[_k: ]
                    k = k - _k
                else:
                    k = k - len(m)
                    m = []
                    
            elif len(m) > _k and len(n) < _k:
                if n[-1] > m[_k-1]:
                    m = m[_k: ]
                    k = k - _k
                else:
                    k = k - len(n)
                    n = []

            if k == 1 and len(m) > 0 and len(n) > 0:
                if m[0] < n[0]:
                    m = m[1:]
                else:
                    n = n[1:]
                k = 0

        if len(m) == 0:
            if c % 2 == 0:
                o = (n[k] + n[k+1])/2.0
            else:
                o = n[k]
        elif len(n) == 0:
            if c % 2 == 0:
                o = (m[k] + m[k+1])/2.0
            else:
                o = m[k]

        elif k == 0:
            if c % 2 == 0:
                p = min(m[0], n[0])
                if m[0] < n[0]:
                    m = m[1:]
                else:
                    n = n[1:]
                if len(m) > 0 and len(n) > 0:
                    q = min(m[0], n[0])
                elif len(m) == 0:
                    q = n[0]
                elif len(n) == 0:
                    q = m[0]
                o = (p + q)/2.0
            else:
                if len(m) > 0 and len(n) > 0:
                    o = min(m[0], n[0])
                elif len(m) == 0:
                    o = n[0]
                elif len(n) == 0:
                    o = m[0]

        return o