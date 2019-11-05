# _*_ coding: utf-8 _*_

"""
This is the solution of no. 98 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/validate-binary-search-tree/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/20
"""

from typing import Optional, Union
from PyLeetCode.entity.tree import *


class Solution1:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: bool, true if the BST is valid
        """
        return self._is_valid_bst(root)

    def _is_valid_bst(self,
                      root: Optional[TreeNode],
                      lower: Union[int, float] = float('-inf'),
                      upper: Union[int, float] = float('inf')) -> bool:
        if not root:
            return True
        val = root.val
        if val <= lower or val >= upper:
            return False
        return self._is_valid_bst(root.left, lower, val) and self._is_valid_bst(root.right, val, upper)


class Solution2:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: bool, true if the BST is valid
        """
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            curr, lower, upper = stack.pop()
            if not curr:
                continue
            val = curr.val
            if val <= lower or val >= upper:
                return False
            stack.append((curr.right, val, upper))
            stack.append((curr.left, lower, val))
        return True

    def is_valid_bst_v2(self, root: Optional[TreeNode]) -> bool:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: bool, true if the BST is valid
        """
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            curr, lower, upper = stack.pop()
            val = curr.val
            if val <= lower or val >= upper:
                return False
            if curr.right:
                stack.append((curr.right, val, upper))
            if curr.left:
                stack.append((curr.left, lower, val))
        return True


class Solution3:
    def is_valid_bst(self, root):
        """
        解法三：中序遍历
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 48 ms, faster than 92.06% of Python3 online submissions for Validate Binary Search Tree.
        Memory Usage: 16 MB, less than 25.29% of Python3 online submissions for Validate Binary Search Tree.

        :param root: TreeNode, the root of BST
        :return: bool, true if the BST is valid
        """
        stack, curr, val = [], root, float('-inf')
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if node.val <= val:
                    return False
                val = node.val
                curr = node.right
        return True

    def is_valid_bst_v2(self, root):
        """
        解法三：中序遍历
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 48 ms, faster than 92.06% of Python3 online submissions for Validate Binary Search Tree.
        Memory Usage: 16.1 MB, less than 24.14% of Python3 online submissions for Validate Binary Search Tree.

        :param root: TreeNode, the root of BST
        :return: bool, true if the BST is valid
        """
        stack, curr = [], root
        val = float('-inf')
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val <= val:
                return False
            val = node.val
            curr = node.right
        return True
