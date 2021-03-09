# _*_ coding: utf-8 _*_

"""
This is the solution of no. 206 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/reverse-linked-list/

The description of problem is as follow:
==========================================================================================================
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
==========================================================================================================

Difficulty: Easy
Tags: linked list;

Author: Genpeng Xu (xgp1227atgmail.com)
Date:   2019/03/28
"""

from PyLeetCode.entity.list import generate_linked_list


class Solution1:
    def reverse_list(self, head):
        """
        解法一：迭代
        时间复杂度：O(n)，其中n为链表的长度
        空间复杂度：O(1)

        Args:
            head: ListNode, the head of linked list

        Returns:
            ListNode, the head of the reversed order linked list
        """
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


class Solution2:
    def reverse_list(self, head):
        """
        解法二：递归
        时间复杂度：O(n)，其中n为链表的长度
        空间复杂度：O(n)，额外的空间是由于递归占用系统栈空间，递归深度最多为n

        Args:
            head: ListNode, the head of linked list

        Returns:
            ListNode, the head of the reversed order linked list
        """
        if not head or not head.next:
            return head
        new_head = self.reverse_list(head.next)
        head.next.next, head.next = head, None
        return new_head


def test():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution2()).reverse_list(head))


if __name__ == '__main__':
    test()
