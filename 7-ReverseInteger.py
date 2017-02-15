# coding: utf-8
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        r = 0
        while y > 0:
            s = y%10
            y = y//10
            r = r*10+s

        if r > 2**31:
            return 0
        if x < 0:
            r = -r

        return r