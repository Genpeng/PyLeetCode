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

from PyLeetCode.entity.tree import *


class Solution:
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = map(self.min_depth, (root.left, root.right))
        return 1 + (min(d) or max(d))
