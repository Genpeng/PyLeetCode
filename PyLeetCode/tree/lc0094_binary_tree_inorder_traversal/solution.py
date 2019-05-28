# _*_ coding: utf-8 _*_

"""
This is the solution of no. 94 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/binary-tree-inorder-traversal/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/15
"""

from PyLeetCode.entity.tree import *


class Solution1:
    def inorder_traversal(self, root: TreeNode) -> list:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the inorder traversal of binary tree
        """
        res = []
        self._inorder_traversal(root, res)
        return res

    def _inorder_traversal(self, root: TreeNode, res: list):
        if root is None:
            return
        self._inorder_traversal(root.left, res)
        res.append(root.val)
        self._inorder_traversal(root.right, res)


class Solution2:
    def inorder_traversal(self, root: TreeNode) -> list:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the inorder traversal of binary tree
        """
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def inorder_traversal_v2(self, root: TreeNode) -> list:
        """
        解法二：迭代（推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the inorder traversal of binary tree
        """
        res, stack, curr = [], [], root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
        return res


class Solution3:
    def inorder_traversal(self, root: TreeNode) -> list:
        """
        解法三：Morris Traversal
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the inorder traversal of binary tree
        """
        res = []
        curr = root
        while curr:
            if curr.left:  # has a left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr
                tmp = curr
                curr = curr.left
                tmp.left = None
            else:
                res.append(curr.val)
                curr = curr.right
        return res
