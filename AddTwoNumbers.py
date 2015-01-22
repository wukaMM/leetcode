"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
        prev = None
        l = last = ListNode(0)
        forward = 0
        
        while l1 != None or l2 != None or forward == 1 :
            if l1 == None:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
                
            if l2 == None:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
                
            ret = v1 + v2 + forward
            if ret >= 10:
                forward = 1
                ret = ret % 10
            else:
                forward = 0
            
            last.val = ret
            last.next = ListNode(0)
            prev = last
            last = last.next
            
        
        prev.next = None
    
        return l
