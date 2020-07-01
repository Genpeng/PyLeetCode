# _*_ coding: utf-8 _*_

"""
This is the solution of no. 88 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/merge-sorted-array/

The description of problem is as follow:
==========================================================================================================
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
- The number of elements initialized in nums1 and nums2 are m and n respectively.
- You may assume that nums1 has enough space (size that is greater or equal to m + n) to
hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/28
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    solution = Solution()
    print(nums1)
    print(nums2)
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    print(nums2)
