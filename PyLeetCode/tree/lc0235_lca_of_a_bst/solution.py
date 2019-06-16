# _*_ coding: utf-8 _*_

"""
This is the solution of no. 235 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

The description of problem is as follow:
==========================================================================================================
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
according to the LCA definition.

Note:
- All of the nodes' values will be unique.
- p and q are different and both values will exist in the BST.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/16
"""

from PyLeetCode.entity.tree import *


class Solution1:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a BST
        :param p: TreeNode, one node in the BST
        :param q: TreeNode, the other node in the BST
        :return: TreeNode, the lowest common ancestor (LCA) of two given nodes in the BST
        """
        if p.val < root.val > q.val:
            return self.lowest_common_ancestor(root.left, p, q)
        elif p.val > root.val < q.val:
            return self.lowest_common_ancestor(root.right, p, q)
        return root

    def lowest_common_ancestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a BST
        :param p: TreeNode, one node in the BST
        :param q: TreeNode, the other node in the BST
        :return: TreeNode, the lowest common ancestor (LCA) of two given nodes in the BST
        """
        if (root.val - p.val) * (root.val - q.val) > 0:
            return self.lowest_common_ancestor((root.left, root.right)[root.val < p.val], p, q)
        else:
            return root


class Solution2:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        解法二：迭代
        时间复杂度：O(n)
        空间复杂度：O(1)

        :param root: TreeNode, the root of a BST
        :param p: TreeNode, one node in the BST
        :param q: TreeNode, the other node in the BST
        :return: TreeNode, the lowest common ancestor (LCA) of two given nodes in the BST
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
            # root = root.left if root.val > p.val else root.right
        return root
