# _*_ coding: utf-8 _*_

"""
This is the solution of no. xxx problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/move-zeroes/

The description of problem is as follow:
==========================================================================================================
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2018/12/07
"""


class Solution1:
    def moveZeroes(self, nums):
        """
        解法一：
        新建一个数组（元素全为0），然后原数组的非零元素保存到新数组的前面，
        最后再用新数组覆盖原数组

        时间复杂度：O(n)
        空间复杂度：O(n)

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * len(nums)
        i = 0
        for num in nums:
            if num != 0:
                tmp[i] = num
                i += 1
        for i in range(len(nums)):
            nums[i] = tmp[i]


class Solution2:
    def moveZeroes(self, nums):
        """
        解法二：
        将数组中非零元素移动到数组前面，然后再将后面的所有元素置为0

        时间复杂度：O(n)
        空间复杂度：O(1)

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1


class Solution3:
    def moveZeroes(self, nums):
        """
        思路三：双指针

        时间复杂度：O(n)
        空间复杂度：O(1)

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


def main():
    nums = [0, 1, 0, 3, 12]
    print(nums)
    (Solution3()).moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
