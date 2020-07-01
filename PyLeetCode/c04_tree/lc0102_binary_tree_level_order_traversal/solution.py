# _*_ coding: utf-8 _*_

"""
This is the solution of no. 102 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/binary-tree-level-order-traversal/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/23
"""

from collections import deque
from typing import Optional, List
from PyLeetCode.entity.tree import *


class Solution1:
    def level_order_v1(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法一：迭代（推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 28 ms, faster than 97.23% of Python3 online submissions for Binary Tree Level Order Traversal.
        Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.

        :param root: TreeNode, the root of a binary tree
        :return: list[list[int]], the level order traversal of its nodes' values
        """
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals)
        return ans

    def level_order_v2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法一：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a binary tree
        :return: list[list[int]], the level order traversal of its nodes' values
        """
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [leaf for leaf in tmp if leaf]
        return res

    def level_order_v3(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法一：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a binary tree
        :return: list[list[int]], the level order traversal of its nodes' values
        """
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [k for n in level for k in (n.left, n.right) if k]
        return res


class Solution2:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法二：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a binary tree
        :return: list[list[int]], the level order traversal of its nodes' values
        """
        res = []
        self._level_order_helper(root, 0, res)
        return res

    def _level_order_helper(self, root: Optional[TreeNode], depth: int, res: List[List[int]]) -> None:
        if not root:
            return
        if depth >= len(res):
            res.append([])
        res[depth].append(root.val)
        self._level_order_helper(root.left, depth + 1, res)
        self._level_order_helper(root.right, depth + 1, res)
