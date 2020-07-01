# _*_ coding: utf-8 _*_

"""
This is the solution of no. 236 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

The description of problem is as follow:
==========================================================================================================
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:
- All of the nodes’ values will be unique.
- p and q are different and both values will exist in the binary tree.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/11
"""

from typing import Optional
from PyLeetCode.entity.tree import *


class Solution1:
    def lowest_common_ancestor(self,
                               root: Optional[TreeNode],
                               p: Optional[TreeNode],
                               q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a binary tree
        :param p: TreeNode, one node in the binary tree
        :param q: TreeNode, other node in the binary tree
        :return: TreeNode, the lowest common ancestor of two nodes
        """
        if not root or root == p or root == q:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        return left or right

    # ========================================================================================= #
    # 下面递归的另一种写法

    def __init__(self):
        self._lca = None

    def lowest_common_ancestor_v2(self,
                                  root: Optional[TreeNode],
                                  p: Optional[TreeNode],
                                  q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法一：递归
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 76 ms, faster than 94.13% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
        Memory Usage: 23 MB, less than 91.67% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

        :param root: TreeNode, the root of a binary tree
        :param p: TreeNode, one node in the binary tree
        :param q: TreeNode, other node in the binary tree
        :return: TreeNode, the lowest common ancestor of two nodes
        """
        if not p or not q:
            raise Exception("[ERROR] The input nodes must not be null!!!")
        if not root:
            return None
        self._find_lca(root, p, q)
        return self._lca

    def _find_lca(self,
                  root: Optional[TreeNode],
                  p: Optional[TreeNode],
                  q: Optional[TreeNode]) -> bool:
        if not root:
            return False
        mid = 1 if root == p or root == q else 0
        left = 1 if self._find_lca(root.left, p, q) else 0
        right = 1 if self._find_lca(root.right, p, q) else 0
        if mid + left + right >= 2:
            self._lca = root
        return mid + left + right > 0


class Solution2:
    def lowest_common_ancestor(self,
                               root: Optional[TreeNode],
                               p: Optional[TreeNode],
                               q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法二：迭代（记录两个节点的路径）
        时间复杂度：O(n)
        空间复杂度：O(n)

        Runtime: 60 ms, faster than 99.98% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
        Memory Usage: 16.5 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

        :param root: TreeNode, the root of a binary tree
        :param p: TreeNode, one node in the binary tree
        :param q: TreeNode, other node in the binary tree
        :return: TreeNode, the lowest common ancestor of two nodes
        """
        if not p or not q:
            raise Exception("[ERROR] The input nodes must not be null!!!")
        if not root:
            return None
        child_2_parent, stack = {root: None}, [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                child_2_parent[node.right] = node
            if node.left:
                stack.append(node.left)
                child_2_parent[node.left] = node
            if p in child_2_parent and q in child_2_parent:
                break
        ancestors = set()
        while p:
            ancestors.add(p)
            p = child_2_parent[p]
        while q and q not in ancestors:
            q = child_2_parent[q]
        return q


class Solution3:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0

    def lowest_common_ancestor(self,
                               root: Optional[TreeNode],
                               p: Optional[TreeNode],
                               q: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        解法二：迭代（不推荐）
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param root: TreeNode, the root of a binary tree
        :param p: TreeNode, one node in the binary tree
        :param q: TreeNode, other node in the binary tree
        :return: TreeNode, the lowest common ancestor of two nodes
        """
        stack = [(root, Solution3.BOTH_PENDING)]
        one_node_found = False
        lca_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution3.BOTH_DONE:
                if parent_state == Solution3.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[lca_index][0]
                        else:
                            one_node_found = True
                            lca_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution3.BOTH_PENDING))
            else:  # parent_state == BOTH_DONE
                if one_node_found and len(stack) - 1:
                    lca_index = -1
                stack.pop()
        return None
