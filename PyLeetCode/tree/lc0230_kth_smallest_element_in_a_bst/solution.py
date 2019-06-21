# _*_ coding: utf-8 _*_

"""
This is the solution of no. 230 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

The description of problem is as follow:
==========================================================================================================
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
- What if the BST is modified (insert/delete operations) often and you need to find
the kth smallest frequently? How would you optimize the kthSmallest routine?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/21
"""

from PyLeetCode.entity.tree import *


class Solution1:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """
        解法一：中序遍历二叉搜索树，并将遍历的结果存储起来，返回结果中索引为k-1的元素即为第k小的元素
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :param k: int, an integer used to specify the element we want to fetch
        :return: int, the kth smallest element
        """
        elements, stack = [], []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                elements.append(node.val)
                curr = node.right
        return elements[k-1]


class Solution2:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """
        解法二：解法二在解法一的基础上进行改进，同样地，中序遍历二叉搜索树，但是当遍历到第k个元素时就停止遍历
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :param k: int, an integer used to specify the element we want to fetch
        :return: int, the kth smallest element
        """
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                curr = node.right
        raise Exception("[ERROR] The value of k is illegal!!!")
