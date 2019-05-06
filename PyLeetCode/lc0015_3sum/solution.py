# _*_ coding: utf-8 _*_

"""
This is the solution of no. 15 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/3sum/

The description of problem is as follow:
==========================================================================================================
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/05/05
"""


class Solution1:
    def three_sum(self, nums: list) -> list:
        """
        解法一：哈希表
        时间复杂度：O(n^2)
        空间复杂度：O(n)

        :param nums: list[int], input array
        :return: list[list[int]], all unique triplets in the array which gives the sum of zero
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, a in enumerate(nums[:-2]):
            if i > 0 and nums[i - 1] == a:
                continue
            s = set()
            for b in nums[i + 1:]:
                if b not in s:
                    s.add(-a - b)
                else:
                    res.add((a, -a - b, b))
        return list(map(list, res))


class Solution2:
    def three_sum(self, nums: list) -> list:
        """
        解法二：双指针
        时间复杂度：O(n^2)
        空间复杂度：O(1)

        :param nums: list[int], input array
        :return: list[list[int]], all unique triplets in the array which gives the sum of zero
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l, r = l + 1, r - 1
        return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print((Solution2()).three_sum(nums))


if __name__ == '__main__':
    main()
