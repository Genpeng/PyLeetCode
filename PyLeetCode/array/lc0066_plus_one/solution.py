# _*_ coding: utf-8 _*_

"""
This is the solution of no. 66 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/plus-one/

The description of problem is as follow:
==========================================================================================================
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element
in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/03/11
"""


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == '__main__':
    digits = [9, 9, 9]
    print((Solution()).plusOne(digits))
