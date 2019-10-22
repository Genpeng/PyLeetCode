# _*_ coding: utf-8 _*_

"""
This is the solution of no. 111 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/minimum-depth-of-binary-tree/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/19
"""

from collections import deque
from typing import Optional
from PyLeetCode.entity.tree import *


class Solution1:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the minimum depth of the binary tree
        """
        if not root:
            return 0
        d = map(self.min_depth, (root.left, root.right))
        return 1 + (min(d) or max(d))

    def min_depth_v2(self, root: Optional[TreeNode]) -> int:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the minimum depth of the binary tree
        """
        if not root:
            return 0
        l, r = self.min_depth_v2(root.left), self.min_depth_v2(root.right)
        return 1 + (min(l, r) or max(l, r))

    def min_depth_v3(self, root: Optional[TreeNode]) -> int:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the minimum depth of the binary tree
        """
        if not root:
            return 0
        if not root.left:
            return 1 + self.min_depth_v3(root.right)
        if not root.right:
            return 1 + self.min_depth_v3(root.left)
        return 1 + min(self.min_depth_v3(root.left), self.min_depth_v3(root.right))


class Solution2:
    def min_depth(self, root: Optional[TreeNode]) -> int:
        """
        解法二：迭代（BFS版本）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the minimum depth of the binary tree
        """
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
