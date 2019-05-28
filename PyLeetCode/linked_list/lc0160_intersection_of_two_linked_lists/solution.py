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


class Solution1:
    def get_intersection_node(self, head_a, head_b):
        """
        解法一：哈希表
        时间复杂度：O(m + n)，其中m和n分别表示两个链表的长度
        空间复杂度：O(m) or O(n)

        :param head_a: ListNode, the head of one of the two linked list
        :param head_b: ListNode, the other head of the two linked list
        :return: ListNode, the intersection node
        """
        nodes_has_seen = set()
        pa, pb = head_a, head_b
        while pa:
            nodes_has_seen.add(pa)
            pa = pa.next
        while pb:
            if pb in nodes_has_seen:
                return pb
            pb = pb.next
        return None


class Solution2:
    def get_intersection_node(self, head_a, head_b):
        """
        解法二：双指针
        时间复杂度：O(L1 + L2 + L3)，具体分析见：https://blog.csdn.net/x273591655/article/details/83409873
        空间复杂度：O(1)

        :param head_a: ListNode, the head of one of the two linked list
        :param head_b: ListNode, the other head of the two linked list
        :return: ListNode, the intersection node
        """
        pa, pb = head_a, head_b
        while pa != pb:
            pa = pa.next if pa else head_b
            pb = pb.next if pb else head_a
        return pa
