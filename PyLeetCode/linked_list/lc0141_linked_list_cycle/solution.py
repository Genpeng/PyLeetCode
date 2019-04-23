# _*_ coding: utf-8 _*_

"""
This is the solution of no. 141 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/linked-list-cycle/

The description of problem is as follow:
==========================================================================================================
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/31
"""

from PyLeetCode.entity.list import *


class Solution1:
    def has_cycle(self, head):
        """
        解法一：哈希表
        时间复杂度：O(n)，其中n表示链表的节点数目
        空间复杂度：O(n)，最多需要存储所有链表的节点

        :param head: ListNode, the head of linked list
        :return: boolean, true if the linked list has a cycle
        """
        nodes_has_seen = set()
        curr = head
        while curr:
            if curr in nodes_has_seen:
                return True
            nodes_has_seen.add(curr)
            curr = curr.next
        return False


class Solution2:
    def has_cycle(self, head):
        """
        解法二：双指针
        时间复杂度：O(n)，详细分析见：https://blog.csdn.net/x273591655/article/details/83343679
        空间复杂度：O(1)，只需要存储两个节点的引用

        :param head: ListNode, the head of linked list
        :return: boolean, true if the linked list has a cycle
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


def main():
    head1 = generate_linked_list([1, 2, 3, 4])
    print((Solution2()).has_cycle(head1))

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = head2
    print((Solution2()).has_cycle(head2))


if __name__ == '__main__':
    main()
