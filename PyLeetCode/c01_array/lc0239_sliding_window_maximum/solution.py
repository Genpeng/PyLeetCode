# _*_ coding: utf-8 _*_

"""
This is the solution of no. 239 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/sliding-window-maximum/

The description of problem is as follow:
==========================================================================================================
Given an array nums, there is a sliding window of size k which is moving from the very left of the array
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]

Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/28
"""

import heapq


class Solution1:
    def max_sliding_window(self, nums: list, k: int) -> list:
        """
        解法一：最大堆
        时间复杂度：O(n * k)，其中n表示数组的大小
        空间复杂度：O(n)

        :param nums: list[int], input array
        :param k: int, the window size
        :return: list[int], all the maximums in the sliding windows
        """
        is_k_illegal = k <= 0 or k > len(nums)
        if nums is None or is_k_illegal:
            raise Exception("[ERROR] The input array is null, or the value of k is illegal!!!")

        pq, res = [], []
        for i, x in enumerate(nums):
            if i <= k - 1:
                heapq.heappush(pq, -x)
            else:
                pq.remove(-nums[i-k])
                heapq.heapify(pq)
                heapq.heappush(pq, -x)
            if i >= k - 1:
                res.append(-pq[0])
        return res


class Solution2:
    def max_sliding_window(self, nums: list, k: int) -> list:
        """
        解法二：使用双端队列模拟滑动窗口
        时间复杂度：O(n)，其中n为数组的长度
        空间复杂度：O(n)

        :param nums: list[int], input array
        :param k: int, the window size
        :return: list[int], all the maximums in the sliding windows
        """
        is_k_illegal = k <= 0 or k > len(nums)
        if nums is None or is_k_illegal:
            raise Exception("[ERROR] The input array is null, or the value of k is illegal!!!")

        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] < x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


def main():
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    solution = Solution2()
    print(solution.max_sliding_window(nums, k))


if __name__ == '__main__':
    main()
