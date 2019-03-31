# _*_ coding: utf-8 _*_

"""
This is the solution of no. 142 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/linked-list-cycle-ii/

The description of problem is as follow:
==========================================================================================================
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/31
"""


class Solution1:
    def detect_cycle(self, head):
        """
        解法一：哈希表
        时间复杂度：O(n)，其中n表示链表节点的数目
        空间复杂度：O(n)

        :param head: ListNode, the head of linked list
        :return: ListNode, the node where the cycle begins
        """
        curr = head
        nodes_has_seen = set()
        while curr:
            if curr in nodes_has_seen:
                return curr
            nodes_has_seen.add(curr)
            curr = curr.next
        return curr


class Solution2:
    def detect_cycle(self, head):
        """
        解法二：双指针
        时间复杂度：O(n)，其中n表示链表节点的数目
        空间复杂度：O(1)，只需要存储三个节点的引用

        :param head: ListNode, the head of linked list
        :return: ListNode, the node where the cycle begins
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow2 = head
                while slow != slow2:
                    slow, slow2 = slow.next, slow2.next
                return slow
        return None
