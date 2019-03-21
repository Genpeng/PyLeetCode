# _*_ coding: utf-8 _*_

"""
Some Linked List classes.

Author: Genpeng Xu
Date:   2019/03/20
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        vals, curr = [], self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        vals.append('null')
        return ' -> '.join(vals)


def generate_linked_list(nums):
    dummy_head = ListNode(-1)
    curr = dummy_head
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy_head.next


if __name__ == '__main__':
    # Linked List 1 -> 2 -> 3 -> null
    nums = [1, 2, 3]
    print(generate_linked_list(nums))