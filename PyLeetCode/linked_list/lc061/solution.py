# _*_ coding: utf-8 _*_

"""
This is the solution of no. xxx problem in the LeetCode,
where the website of the problem is as follow:
xxx

The description of problem is as follow:
==========================================================================================================
xxx
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/01
"""

from PyLeetCode.entity.list import *


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
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


def main():
    head = generate_linked_list([1, 2, 3, 4, 5])
    print(head)
    print((Solution()).rotateRight(head, 2))


if __name__ == '__main__':
    main()
