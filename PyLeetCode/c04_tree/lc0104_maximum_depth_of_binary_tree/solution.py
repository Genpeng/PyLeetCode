# _*_ coding: utf-8 _*_

"""
This is the solution of no. 104 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/maximum-depth-of-binary-tree/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/20
"""

from typing import Optional
from collections import deque
from PyLeetCode.entity.tree import *


class Solution1:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the maximum depth of the binary tree
        """
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


class Solution2:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        解法二：迭代（DFS版本）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the maximum depth of the binary tree
        """
        if not root:
            return 0
        s1, s2, max_depth = [], [], 0
        s1.append(root)
        s2.append(1)
        while s1:
            node = s1.pop()
            depth = s2.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                s1.append(node.left)
                s2.append(depth + 1)
            if node.right:
                s1.append(node.right)
                s2.append(depth + 1)
        return max_depth

    def max_depth_v2(self, root: Optional[TreeNode]) -> int:
        """
        解法二：迭代（DFS版本）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the maximum depth of the binary tree
        """
        if not root:
            return 0
        s, max_depth = [], 0
        s.append((root, 1))
        while s:
            node, depth = s.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                s.append((node.left, depth + 1))
            if node.right:
                s.append((node.right, depth + 1))
        return max_depth


class Solution3:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        解法二：迭代（BFS版本）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the maximum depth of the binary tree
        """
        if not root:
            return 0
        q, depth = deque([root]), 0
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
