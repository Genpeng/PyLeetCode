# _*_ coding: utf-8 _*_

"""
This is the solution of no. 350 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/intersection-of-two-arrays-ii/

The description of problem is as follow:
==========================================================================================================
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/16
"""


class Solution1:
    def intersect(self, nums1, nums2):
        """
        解法：
        用Map存储数组1中元素出现的次数，之后遍历数组2，如果数组2中的元素在数组1中出现，
        次数减1，并保存该元素

        时间复杂度：O(n)
        空间复杂度：O(n)

        :param nums1: one of the integer array
        :param nums2: the other integer array
        :return: the intersection of two array
        """
        if not nums1 or not nums2:
            return []

        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        res = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                res.append(num)
                counts[num] -= 1
        return res



class Solution2:
    def intersect(self, nums1, nums2):
        """
        解法：双指针
        时间复杂度：O(n * logn)
        空间复杂度：O(1)

        :param nums1: one of the integer array
        :param nums2: the other integer array
        :return: the intersection of two array
        """
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:  # nums1[i] > nums2[j]
                j += 1
        return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print((Solution1()).intersect(nums1, nums2))
