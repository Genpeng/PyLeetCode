# _*_ coding: utf-8 _*_

"""
This is the solution of no. 148 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/sort-list/

The description of problem is as follow:
==========================================================================================================
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/30
"""

from typing import Tuple, Optional
from PyLeetCode.entity.list import *


class Solution1:
    def sort_list(self, head: ListNode) -> ListNode:
        """
        解法一：取出链表的所有元素，排序后生成一个新的链表
        时间复杂度：O(n * log(n))
        空间复杂度：O(n)

        Parameters
        ----------
        head: ListNode, the head of the linked list

        Return
        ------
        ListNode, the head of the sorted list
        """
        if not head or not head.next:
            return head
        # 1. 取出链表的元素
        vals, curr = [], head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        # 2. 排序
        vals.sort()
        # 3. 生成新链表
        dummy_head = ListNode(-1)
        prev = dummy_head
        for val in vals:
            prev.next = ListNode(val)
            prev = prev.next
        return dummy_head.next


class Solution2:
    def sort_list(self, head: ListNode) -> ListNode:
        """
        解法二：归并排序（Top down）
        时间复杂度：O(n * log(n))
        空间复杂度：O(log(n))

        Parameters
        ----------
        head: ListNode, the head of the linked list

        Return
        ------
        ListNode, the head of the sorted list
        """
        # Recursion termination condition
        if not head or not head.next:
            return head
        # split the long linked list into two short list
        head, head2 = self.split_list(head)
        # Split the linked list into two halves
        l1 = self.sort_list(head)
        l2 = self.sort_list(head2)
        # Merge two sorted list into a list
        return self.merge_two_lists(l1, l2)

    def split_list(self, head: ListNode) -> Tuple[ListNode, ListNode]:
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        return head, slow

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        prev = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy_head.next


class Solution3:
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法三：归并排序（Bottom up）
        时间复杂度：O(n * log(n))
        空间复杂度：O(1)

        Parameters
        ----------
        head: ListNode, the head of the linked list

        Return
        ------
        ListNode, the head of the sorted list
        """
        if not head or not head.next:
            return head
        # Count the length of linked list
        n, curr = 0, head
        while curr:
            n, curr = n + 1, curr.next
        # Split the linked list into sublist with different length, and merge them
        dummy_head = ListNode(-1)
        dummy_head.next = head
        i = 1
        while i < n:
            tail, curr = dummy_head, dummy_head.next
            while curr:
                l = curr
                r = self._split(l, i)
                curr = self._split(r, i)
                pair = self._merge(l, r)
                tail.next = pair[0]
                tail = pair[1]
            i <<= 1
        return dummy_head.next

    def _split(self, head: ListNode, n: int) -> Optional[ListNode]:
        while n > 1 and head:
            n, head = n - 1, head.next
        rest = head.next if head else None
        if head:
            head.next = None
        return rest

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
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
        while tail.next:
            tail = tail.next
        return dummy_head.next, tail


if __name__ == '__main__':
    # test `sort_list` method
    head = generate_linked_list([4, 2, 1, 3])
    print(head)
    solution = Solution3()
    new_head = solution.sort_list(head)
    print(new_head)
