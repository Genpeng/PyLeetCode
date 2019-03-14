# _*_ coding: utf-8 _*_

"""
This is the solution of no. 169 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/majority-element/

The description of problem is as follow:
==========================================================================================================
Given an array of size n, find the majority element. The majority element is the element that
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/14
"""


class Solution1:
    """
    解法：使用Map记录数字的次数
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def majority_element(self, nums):
        threshold, counts = len(nums) // 2, dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > threshold:
                return num
        raise Exception("The majority element does not exist!!!")

    def majority_element_1(self, nums):
        threshold, counts = len(nums) // 2, dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return max(counts, key=counts.get)


class Solution2:
    """
    解法：对数组进行排序，取索引为⌊n/2⌋的数字
    时间复杂度：O(n * logn)
    空间复杂度：O(n) or O(1), 取决于是否可以直接对数组进行排序
    """
    def majority_element(self, nums):
        return sorted(nums)[len(nums) // 2]


class Solution3:
    """
    解法：多数投票算法（Boyer-Moore majority vote algorithm）
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def majority_element(self, nums):
        m, count = 0, 0
        for num in nums:
            if count == 0:
                m, count = num, 1
            elif m == num:
                count += 1
            else:
                count -= 1
        return m


if __name__ == '__main__':
    nums = [2, 2, 2, 1, 1, 1, 2]
    print((Solution3()).majority_element(nums))
