# _*_ coding: utf-8 _*_

"""
This is the solution of no. 103 problem in the LeetCode,
where the website of the problem is as follow:


The description of problem is as follow:
==========================================================================================================
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right,
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/10/19
"""

from collections import deque
from typing import Optional, List
from PyLeetCode.entity.tree import *


class Solution1:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法一：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 32 ms, faster than 85.41% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

        :param root: TreeNode, the root of the binary tree
        :return: the zigzag level order traversal of its nodes' values
        """
        res = []
        if not root:
            return res
        q, is_right = deque([root]), True
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if is_right:
                res.append(vals)
            else:
                res.append(vals[::-1])
            is_right = not is_right
        return res


class Solution2:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        解法二：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of the binary tree
        :return: the zigzag level order traversal of its nodes' values
        """
        res = []
        self._zigzag_level_order(root, 0, res)
        return res

    def _zigzag_level_order(self, root: Optional[TreeNode], depth: int, res: List[List[int]]) -> None:
        if not root:
            return
        if depth >= len(res):
            res.append([])
        vals = res[depth]
        if depth & 1 == 0:
            vals.append(root.val)
        else:
            vals.insert(0, root.val)
        self._zigzag_level_order(root.left, depth + 1, res)
        self._zigzag_level_order(root.right, depth + 1, res)
