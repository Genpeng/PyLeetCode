# _*_ coding: utf-8 _*_

"""
This is the solution of no. 226 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/invert-binary-tree/

The description of problem is as follow:
==========================================================================================================
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree
on a whiteboard so f*** off.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/20
"""

from collections import deque
from typing import Optional
from PyLeetCode.entity.tree import *


class Solution1:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: TreeNode, the root of inverted binary tree
        """
        if not root:
            return root
        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root


class Solution2:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法二：迭代（DFS）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: TreeNode, the root of inverted binary tree
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


class Solution3:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法三：迭代（BFS）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: TreeNode, the root of inverted binary tree
        """
        if not root:
            return root
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                # swap left and right subtree
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
