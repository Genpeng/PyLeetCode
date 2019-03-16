# _*_ coding: utf-8 _*_

"""
This is the solution of no. 724 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/find-pivot-index/

The description of problem is as follow:
==========================================================================================================
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to
the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return
the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.


Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


Note:
The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/17
"""


class Solution:
    def pivot_index(self, nums):
        if nums is None:
            raise Exception("[ERROR] The input array is None!!!")

        s, left_sum = sum(nums), 0
        for i in range(len(nums)):
            if left_sum == s - nums[i] - left_sum:
                return i
            left_sum += nums[i]
        return -1


if __name__ == '__main__':
    nums = [-1, -1, -1, 0, 1, 1]
    print((Solution()).pivot_index(nums))
