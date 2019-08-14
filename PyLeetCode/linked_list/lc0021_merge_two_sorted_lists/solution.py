# _*_ coding: utf-8 _*_

"""
This is the solution of no. 21 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/merge-two-sorted-lists/

The description of problem is as follow:
==========================================================================================================
Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/27
"""

from PyLeetCode.entity.list import *


class Solution1:
    def merge_two_lists(self, l1, l2):
        """
        解法一：迭代
        时间复杂度：O(n)
        空间复杂度：O(1)

        :param l1: one of two linked lists
        :param l2: the other linked list
        :return: the merged linked list
        """
        dummy_head = ListNode(-1)
        tail = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy_head.next


class Solution2:
    def merge_two_lists(self, l1, l2):
        """
        解法二：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param l1: one of two linked lists
        :param l2: the other linked list
        :return: the merged linked list
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2


def main():
    l1 = generate_linked_list([1, 2, 4])
    l2 = generate_linked_list([1, 3, 4])
    print((Solution2()).merge_two_lists(l1, l2))


if __name__ == '__main__':
    main()
