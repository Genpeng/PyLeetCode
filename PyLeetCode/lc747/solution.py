# _*_ coding: utf-8 _*_

"""
This is the solution of no. 747 problem in the LeetCode,
where the website of the problem is as follow:


The description of problem is as follow:
==========================================================================================================
In a given integer array `nums`, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the **index** of the largest element, otherwise return -1.

**Example 1:**

```
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
```



**Example 2:**

```
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
```



**Note:**

1. `nums` will have a length in the range `[1, 50]`.
2. Every `nums[i]` will be an integer in the range `[0, 99]`.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/18
"""


class Solution:
    def dominant_index_1(self, nums):
        # 1. 找出最大值的索引
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i

        # 2. 判断最大值是否是其他元素的两倍以上
        for i in range(len(nums)):
            if i != max_index and nums[max_index] < 2 * nums[i]:
                return -1
        return max_index

    def dominant_index_2(self, nums):
        max_num = max(nums)
        if all(max_num >= 2 * num for num in nums if num != max_num):  # all([]) = True
            return nums.index(max_num)
        return -1


if __name__ == '__main__':
    nums1 = [6]
    nums2 = [3, 6, 1, 0]
    print((Solution()).dominant_index_2(nums1))
