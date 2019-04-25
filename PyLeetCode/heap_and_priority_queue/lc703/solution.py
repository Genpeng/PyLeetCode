# _*_ coding: utf-8 _*_

"""
This is the solution of no. 703 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/kth-largest-element-in-a-stream/

The description of problem is as follow:
==========================================================================================================
Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/18
"""

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self._pool = nums
        self._k = k
        heapq.heapify(self._pool)
        while len(self._pool) > k:
            heapq.heappop(self._pool)

    def add(self, val):
        if len(self._pool) < self._k:
            heapq.heappush(self._pool, val)
        elif val > self._pool[0]:
            heapq.heapreplace(self._pool, val)
        return self._pool[0]


def main():
    k = 3
    nums = [4, 5, 8, 2]
    kth_largest = KthLargest(3, nums)
    print(kth_largest.add(3))
    print(kth_largest.add(5))
    print(kth_largest.add(10))
    print(kth_largest.add(9))
    print(kth_largest.add(4))


if __name__ == '__main__':
    main()
