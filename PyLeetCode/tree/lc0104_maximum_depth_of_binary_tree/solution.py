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

from PyLeetCode.entity.tree import *


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
