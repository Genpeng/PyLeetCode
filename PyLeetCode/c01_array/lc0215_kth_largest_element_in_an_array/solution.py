# _*_ coding: utf-8 _*_

"""
This is the solution of no. 215 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/kth-largest-element-in-an-array/

The description of problem is as follow:
==========================================================================================================
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
- 1 <= k <= nums.length <= 104
- -104 <= nums[i] <= 104
==========================================================================================================

Difficulty: Medium
Tags: array;heap;divide and conquer;

Author: Genpeng Xu (xgp1227atgmail.com)
"""

import heapq
import random
from typing import List


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach 1: Brute Force

        Complexity Analysis:
        Time Complexity: O(n * log(n))
        Space Complexity: O(log(n))

        Args:
            nums: List[int], an integer array
            k: int, an integer

        Returns:
            int, the kth largest element in the array
        """
        nums.sort()
        return nums[len(nums) - k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach 2: Heap

        Complexity Analysis:
        Time Complexity: O(n * log(k))
        Space Complexity: O(k)

        Args:
            nums: List[int], an integer array
            k: int, an integer

        Returns:
            int, the kth largest element in the array
        """
        h = nums[:k]
        heapq.heapify(h)
        for num in nums[k:]:
            if num > h[0]:
                heapq.heapreplace(h, num)
        return h[0]


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach 3: Quick Select (top down)

        Complexity Analysis:
        Time Complexity: O(n)
        Space Complexity: O(log(n))

        Args:
            nums: List[int], an integer array
            k: int, an integer

        Returns:
            int, the kth largest element in the array
        """
        n, ti = len(nums), len(nums) - k
        self.quick_select(nums, 0, n - 1, ti)
        return nums[ti]

    def quick_select(self, nums: List[int], li: int, ri: int, ti: int) -> None:
        if li >= ri:
            return
        split_index = random_partition(nums, li, ri)
        if split_index < ti:
            self.quick_select(nums, split_index + 1, ri, ti)
        elif split_index > ti:
            self.quick_select(nums, li, split_index - 1, ti)


class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Approach 4: Quick Select (bottom up)

        Complexity Analysis:
        Time Complexity: O(n)
        Space Complexity: O(log(n))

        Args:
            nums: List[int], an integer array
            k: int, an integer

        Returns:
            int, the kth largest element in the array
        """
        n, ti = len(nums), len(nums) - k
        li, ri = 0, n - 1
        while li < ri:
            split_index = random_partition(nums, li, ri)
            if split_index == ti:
                break
            elif split_index < ti:
                li = split_index + 1
            else:  # split_index > ti
                ri = split_index - 1
        return nums[ti]


def random_partition(nums: List[int], li: int, ri: int) -> int:
    swap(nums, random.randint(li, ri), ri)
    return partition(nums, li, ri)


def partition(nums: List[int], li: int, ri: int) -> int:
    pivot = nums[ri]
    i = li - 1
    for j in range(li, ri):
        if nums[j] < pivot:
            i += 1
            if i < j:
                swap(nums, i, j)
    i += 1
    swap(nums, i, ri)
    return i


def swap(nums: List[int], i: int, j: int) -> None:
    if i != j:
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    solu = Solution3()
    print(solu.findKthLargest(nums, 2) == 5)
