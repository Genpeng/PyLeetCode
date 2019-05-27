# _*_ coding: utf-8 _*_

"""
This is the solution of no. 19 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

The description of problem is as follow:
==========================================================================================================
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/05
"""

from PyLeetCode.entity.list import *


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head
        # p2指针移动n个节点，使得p1和p2之间的距离为n+1
        for _ in range(n):
            p2 = p2.next
        # 如果p2指针为空，则说明链表的长度刚好为n，待删除的节点刚好为头结点
        if p2 is None:
            return head.next
        # 如果p2不为空，同时移动两个节点，使得p2刚好位于尾节点
        while p2:
            p1 = p1.next
            p2 = p2.next
        # 删除倒数第n个节点
        delete_node = p1.next
        p1.next = delete_node.next
        delete_node.next = None
        return head


def main():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution()).remove_nth_from_end(head, 5))


if __name__ == '__main__':
    main()
