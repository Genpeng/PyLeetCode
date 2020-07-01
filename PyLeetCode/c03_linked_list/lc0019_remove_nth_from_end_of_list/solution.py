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
        # Step 1: move `p2` n times, so that the distance between `p1` and `p2` is n+1
        for _ in range(n):
            p2 = p2.next
        if not p2:
            return head.next
        # Step 2: move `p1` and `p2` simultaneously until `p2.next` is null pointer,
        # this time `p1` is the n+1 node from the end of list
        while p2.next:
            p1, p2 = p1.next, p2.next
        # Step 3: delete n node from the end of list
        p1.next = p1.next.next
        return head


def main():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution()).remove_nth_from_end(head, 5))


if __name__ == '__main__':
    main()
