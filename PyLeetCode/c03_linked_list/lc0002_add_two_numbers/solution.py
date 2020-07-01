# _*_ coding: utf-8 _*_

"""
This is the solution of no. 2 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/add-two-numbers/

The description of problem is as follow:
==========================================================================================================
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/20
"""

from PyLeetCode.entity.list import *


class Solution1:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        解法一：迭代
        时间复杂度：O(max(m,n))，其中m和n分别表示两个链表的长度
        空间复杂度：O(max(m,n))，返回的结果链表长度最大为max(m,n)+1

        :param l1: ListNode, one of the linked list
        :param l2: ListNode, the other linked list
        :return: the result linked list which represents the sum of two 'numbers'
        """
        if not l1 or not l2:
            return l1 or l2
        dummy_head = ListNode(-1)
        tail = dummy_head
        carry = 0
        while l1 or l2:
            s = carry
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0
            tail.next = ListNode(s % 10)
            tail = tail.next
            # update to next iteration
            carry = s // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            tail.next = ListNode(carry)
        return dummy_head.next


class Solution2:
    def add_two_numbers(self, l1, l2):
        """
        解法二：递归
        时间复杂度：O(max(m,n))，其中m和n分别表示两个链表的长度
        空间复杂度：O(max(m,n))，额外空间是由于递归调用占用系统栈的空间，
                  递归深度最多为max(m,n)+1层

        :param l1: ListNode, one of the linked list
        :param l2: ListNode, the other linked list
        :return: the result linked list which represents the sum of two 'numbers'
        """
        return self._add_two_numbers(l1, l2, 0)

    def _add_two_numbers(self, l1, l2, carry):
        # Recursion termination condition
        if not l1 and not l2:
            return ListNode(carry) if carry else None
        s, l1_next, l2_next = carry, None, None
        if l1:
            s += l1.val
            l1_next = l1.next
        if l2:
            s += l2.val
            l2_next = l2.next
        curr = ListNode(s % 10)
        curr.next = self._add_two_numbers(l1_next, l2_next, s // 10)
        return curr


def main():
    l1 = generate_linked_list([2, 4, 3])
    l2 = generate_linked_list([5, 6, 4])
    print((Solution2()).add_two_numbers(l1, l2))


if __name__ == '__main__':
    main()
