# _*_ coding: utf-8 _*_

"""
This is the solution of no. 23 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/merge-k-sorted-lists/

The description of problem is as follow:
==========================================================================================================
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/07/04
"""

import sys
import heapq
from typing import List
from queue import PriorityQueue
from PyLeetCode.entity.list import *


class Solution1:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """
        解法一：Brute Force
        时间复杂度：O(N * log(N))
        空间复杂度：O(N)

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        dummy_head = ListNode(-1)
        tail = dummy_head
        for val in sorted(vals):
            tail.next = ListNode(val)
            tail = tail.next
        return dummy_head.next


class Solution2:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """
        解法二：k指针（双指针的扩展版），即每次将值最小的节点加到结果链表中
        时间复杂度：O(N * k)
        空间复杂度：O(N)

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        dummy_head = ListNode(-1)
        tail = dummy_head
        while True:
            min_index, min_node = -1, ListNode(sys.maxsize)  # or `min_node = ListNode(float('inf'))`
            for i, node in enumerate(lists):
                if node and node.val < min_node.val:
                    min_index, min_node = i, node
            if min_index == -1:
                break
            tail.next = min_node
            # update to next iteration
            tail = tail.next
            lists[min_index] = min_node.next
        return dummy_head.next


class Solution3:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """
        解法三：在解法二的基础上，采用优先队列进行优化
        时间复杂度：O(N * log(k))
        空间复杂度：O(k)

        Note:
        Runtime: 152 ms
        Memory Usage: 16.8 MB
        Your runtime beats 28.13 % of python3 submissions.

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        q = PriorityQueue()
        for i, l in enumerate(lists):  # Time complexity: k * log(k)
            if l:
                q.put((l.val, i))
        dummy_head = ListNode(-1)
        tail = dummy_head
        while not q.empty():
            min_index = q.get()[1]  # Time complexity: O(log(k))
            tail.next = lists[min_index]
            tail = tail.next
            next_node = tail.next
            lists[min_index] = next_node  # update the head of the minimum list
            if next_node:
                q.put((next_node.val, min_index))
        return dummy_head.next

    def merge_k_lists_v2(self, lists: List[ListNode]) -> ListNode:
        """
        解法三：在解法二的基础上，采用优先队列进行优化（推荐）
        时间复杂度：O(N * log(k))
        空间复杂度：O(k)

        Note:
        Runtime: 64 ms
        Memory Usage: 16.3 MB
        Your runtime beats 98.11 % of python3 submissions.

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        pq = []
        for i, node in enumerate(lists):
            if node:
                pq.append((node.val, i))
        heapq.heapify(pq)  # Time complexity: O(k)
        dummy_head = ListNode(-1)
        tail = dummy_head
        while pq:
            _, min_index = heapq.heappop(pq)
            tail.next = lists[min_index]
            tail = tail.next
            next_node = tail.next
            lists[min_index] = next_node
            if next_node:
                heapq.heappush(pq, (next_node.val, min_index))
        return dummy_head.next


class Solution4:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """
        解法四：将问题分解成为合并两个链表（k-1次）
        时间复杂度：O(N * k)
        空间复杂度：O(1)

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        head = lists[0]
        for head2 in lists[1:]:
            head = self._merge_two_lists(head, head2)
        return head

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


class Solution5:
    def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
        """
        解法五：Divide & Conquer, Top down
        时间复杂度：O(N * log(k))
        空间复杂度：O(log(k))

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        if not lists:
            return None
        return self._merge_k_lists(lists, 0, len(lists) - 1)

    def _merge_k_lists(self, lists, si, ei):
        """
        Merge k lists where the start index is `si`, and the end index is `ei`.

        :param lists: list[ListNode], k sorted linked lists
        :param si: int, the start index
        :param ei: int, the end index
        :return: ListNode, the new sorted linked list
        """
        if si == ei:
            return lists[si]
        mi = si + (ei - si) // 2
        l1 = self._merge_k_lists(lists, si, mi)
        l2 = self._merge_k_lists(lists, mi + 1, ei)
        return self._merge_two_lists(l1, l2)

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


class Solution6:
    def merge_k_lists(self, lists):
        """
        解法六：Divide & Conquer, Bottom up
        时间复杂度：O(N * log(k))
        空间复杂度：O(1)

        Q&A:
        调用 `range` 方法时，减去一个 `interval` 的作用是什么？
        为了使得 `range` 方法的输出结果都是偶数个数，而非奇数个数。

        :param lists: list[ListNode], k sorted linked lists
        :return: a new sorted linked list
        """
        if not lists:
            return None
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self._merge_two_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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


if __name__ == '__main__':
    head1 = generate_linked_list([1, 4, 5])
    head2 = generate_linked_list([1, 3, 4])
    head3 = generate_linked_list([2, 6])
    lists = [head1, head2, head3]
    solution = Solution2()
    print(solution.merge_k_lists(lists))
