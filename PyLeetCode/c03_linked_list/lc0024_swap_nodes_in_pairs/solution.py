# _*_ coding: utf-8 _*_

"""
This is the solution of no. 24 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/swap-nodes-in-pairs/

The description of problem is as follow:
==========================================================================================================
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/05
"""

from PyLeetCode.entity.list import *


class Solution1:
    def swap_pairs(self, head: ListNode) -> ListNode:
        """
        解法一：迭代
        时间复杂度：O(n)
        空间复杂度：O(1)

        :param head: ListNode, the head of linked list
        :return: ListNode, the head of modified linked list
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        prev = dummy_head
        while prev.next and prev.next.next:
            p1, p2 = prev.next, prev.next.next
            # swap two nodes
            p1.next, p2.next, prev.next = p2.next, p1, p2
            # update to next iteration
            prev = p1
        return dummy_head.next


class Solution2:
    def swap_pairs(self, head: ListNode) -> ListNode:
        """
        解法二：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param head: ListNode, the head of linked list
        :return: ListNode, the head of modified linked list
        """
        if not head or not head.next:
            return head
        p = head.next
        head.next = self.swap_pairs(head.next.next)
        p.next = head
        return p


def main():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution2()).swap_pairs(head))


if __name__ == '__main__':
    main()
