# _*_ coding: utf-8 _*_

"""
This is the solution of no. 61 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/rotate-list/

The description of problem is as follow:
==========================================================================================================
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/01
"""

from PyLeetCode.entity.list import *


class Solution:
    def rotate_right(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        # 求出链表的长度
        length, curr = 1, head
        while curr.next:
            curr = curr.next
            length += 1

        # 求出实际右移的次数
        k %= length
        if k == 0:
            return head

        # 求出倒数第k+1个节点
        p1, p2 = head, head
        for i in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        # “右移”链表
        new_head = p1.next
        p1.next, p2.next = None, head
        return new_head

    def rotate_right_v2(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # 求出链表长度
        l, curr = 0, head
        while curr:
            l += 1
            curr = curr.next
        # 求出实际需要翻转的次数k
        k = k % l
        if k == 0:
            return head
        # 翻转链表
        return self.rotate_nth_from_end(head, k)

    def rotate_nth_from_end(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        for _ in range(k):
            p2 = p2.next
        while p2.next:
            p1, p2 = p1.next, p2.next
        new_head = p1.next
        p1.next, p2.next = None, head
        return new_head


def main():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution()).rotate_right_v2(head, 2))


if __name__ == '__main__':
    main()
