# _*_ coding: utf-8 _*_

"""
This is the solution of no. 145 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/binary-tree-postorder-traversal/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/16
"""

from typing import Optional, List
from PyLeetCode.entity.tree import *


class Solution1:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the postorder traversal of binary tree
        """
        res = []
        self._postorder_traversal(root, res)
        return res

    def _postorder_traversal(self, root: Optional[TreeNode], res: List[int]) -> None:
        if root is None:
            return
        self._postorder_traversal(root.left, res)
        self._postorder_traversal(root.right, res)
        res.append(root.val)


class Solution2:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of binary tree
        :return: list, the postorder traversal of binary tree
        """
        res, stack, curr = [], [], root
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop().left
        return res[::-1]
