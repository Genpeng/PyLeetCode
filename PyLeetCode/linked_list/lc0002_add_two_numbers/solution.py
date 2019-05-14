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
    def add_two_numbers_1(self, l1, l2):
        """
        解法一：迭代
        时间复杂度：O(max(m,n))，其中m和n分别表示两个链表的长度
        空间复杂度：O(max(m,n))，返回的结果链表长度最大为max(m,n)+1

        :param l1: ListNode, one of the linked list
        :param l2: ListNode, the other linked list
        :return:
        """
        dummy_head = ListNode(-1)
        curr = dummy_head

        carry, p, q = 0, l1, l2
        while p or q:
            sum = carry
            if p:
                sum += p.val
            if q:
                sum += q.val

            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if p:
                p = p.next
            if q:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy_head.next

    def add_two_numbers_2(self, l1, l2):
        """
        解法一：迭代
        时间复杂度：O(max(m,n))，其中m和n分别表示两个链表的长度
        空间复杂度：O(max(m,n))，返回的结果链表长度最大为max(m,n)+1

        :param l1: ListNode, one of the linked list
        :param l2: ListNode, the other linked list
        :return: the result linked list which represents the sum of two 'numbers'
        """
        dummy_head = ListNode(-1)
        curr = dummy_head

        p, q, carry = l1, l2, 0
        while p or q or carry:
            v1, v2 = 0, 0
            if p:
                v1 = p.val
                p = p.next
            if q:
                v2 = q.val
                q = q.next
            carry, v = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(v)
            curr = curr.next
        return dummy_head.next

    def add_two_numbers_3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        解法一：迭代
        时间复杂度：O(max(m,n))，其中m和n分别表示两个链表的长度
        空间复杂度：O(max(m,n))，返回的结果链表长度最大为max(m,n)+1

        :param l1: ListNode, one of the linked list
        :param l2: ListNode, the other linked list
        :return: the result linked list which represents the sum of two 'numbers'
        """
        dummy_head = ListNode(-1)
        p1, p2, prev = l1, l2, dummy_head
        carry = 0
        while p1 or p2:
            s = carry
            s += 0 if p1 is None else p1.val
            s += 0 if p2 is None else p2.val
            prev.next = ListNode(s % 10)
            # update to next iteration
            carry = s // 10
            p1 = p1 if p1 is None else p1.next
            p2 = p2 if p2 is None else p2.next
            prev = prev.next
        if carry > 0:
            prev.next = ListNode(carry)
        return dummy_head.next

    def add_two_numbers_4(self, l1: ListNode, l2: ListNode) -> ListNode:
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
        curr, p1, p2 = dummy_head, l1, l2
        carry = 0
        while p1 or p2:
            s = carry
            s += 0 if not p1 else p1.val
            s += 0 if not p2 else p2.val
            carry = s // 10
            curr.next = ListNode(s % 10)
            # update to next iteration
            p1 = p1 if not p1 else p1.next
            p2 = p2 if not p2 else p2.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
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
        if not l1 and not l2:
            if carry > 0:
                return ListNode(carry)
            else:
                return None

        s = carry
        l1_next, l2_next = None, None
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
