# _*_ coding: utf-8 _*_

"""
This is the solution of no. 203 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/remove-linked-list-elements/

The description of problem is as follow:
==========================================================================================================
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/01
"""

from PyLeetCode.entity.list import *


class Solution:
    def remove_elements(self, head, val):
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev = dummy_head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy_head.next
