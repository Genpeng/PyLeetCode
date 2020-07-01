# _*_ coding: utf-8 _*_

"""
This is the solution of no. 144 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/binary-tree-preorder-traversal/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Follow up: Recursive solution is trivial, could you do it iteratively?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/15
"""

from typing import Optional, List
from PyLeetCode.entity.tree import *


class Solution1:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: list, the preorder traversal of BST
        """
        ans = []
        self._preorder_traversal(root, ans)
        return ans

    def _preorder_traversal(self, root: Optional[TreeNode], ans: List[int]) -> None:
        if root is None:
            return
        ans.append(root.val)
        self._preorder_traversal(root.left, ans)
        self._preorder_traversal(root.right, ans)


class Solution2:
    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: list, the preorder traversal of BST
        """
        ans = []
        if not root:
            return ans
        stack = [root]
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return ans

    def preorder_traversal_v2(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: list, the preorder traversal of BST
        """
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans

    def preorder_traversal_v3(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: list, the preorder traversal of BST
        """
        ans = []
        curr, stack = root, []
        while curr or stack:
            if curr:
                ans.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop().right
        return ans

    def preorder_traversal_v4(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法二：迭代（推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of BST
        :return: list, the preorder traversal of BST
        """
        ans = []
        curr, stack = root, []
        while curr or stack:
            while curr:
                ans.append(curr.val)
                stack.append(curr)
                curr = curr.left
            curr = stack.pop().right
        return ans
