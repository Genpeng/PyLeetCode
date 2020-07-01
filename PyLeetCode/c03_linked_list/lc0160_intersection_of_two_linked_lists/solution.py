# _*_ coding: utf-8 _*_

"""
This is the solution of no. 160 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/intersection-of-two-linked-lists/

The description of problem is as follow:
==========================================================================================================
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/01
"""

from typing import Optional
from PyLeetCode.entity.list import *


class Solution1:
    def get_intersection_node(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法一：哈希表
        时间复杂度：O(m + n)，其中m和n分别表示两个链表的长度
        空间复杂度：O(m) or O(n)

        :param head1: ListNode, the head of one of the two linked list
        :param head2: ListNode, the other head of the two linked list
        :return: ListNode, the intersection node
        """
        nodes_has_seen = set()
        p1, p2 = head1, head2
        while p1:
            nodes_has_seen.add(p1)
            p1 = p1.next
        while p2:
            if p2 in nodes_has_seen:
                return p2
            p2 = p2.next
        return None


class Solution2:
    def get_intersection_node(self, head1, head2):
        """
        解法二：双指针
        时间复杂度：O(L1 + L2 + L3)，具体分析见：https://blog.csdn.net/x273591655/article/details/83409873
        空间复杂度：O(1)

        :param head1: ListNode, the head of one of the two linked list
        :param head2: ListNode, the other head of the two linked list
        :return: ListNode, the intersection node
        """
        p1, p2 = head1, head2
        while p1 != p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1
        return p1
