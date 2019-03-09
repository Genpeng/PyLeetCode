# _*_ coding: utf-8 _*_

"""
This is the solution of no. 1 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/two-sum/

The description of problem is as follow:
==========================================================================================================
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/09
"""


class Solution:
    def twoSum(self, nums, target):
        if not nums or len(nums) == 1:
            raise Exception("[Error] The input array is illegal!")

        comps = dict()
        for i, num in enumerate(nums):
            if num in comps:
                return [comps[num], i]
            else:
                comps[target - num] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print((Solution()).twoSum(nums, target))
