# _*_ coding: utf-8 _*_

"""
This is the solution of no. 412 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/fizz-buzz/

The description of problem is as follow:
==========================================================================================================
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/06/26
"""


class Solution1:
    def fizz_buzz(self, n: int) -> list:
        """
        解法一：条件判断
        时间复杂度：O(n)
        空间复杂度：O(1)

        :param n: int, an integer
        :return: list of string, the string representation of numbers from 1 to n
        """
        res = []
        for i in range(1, n + 1):
            divisible_by_3, divisible_by_5 = i % 3 == 0, i % 5 == 0
            if divisible_by_3 and divisible_by_5:
                res.append("FizzBuzz")
            elif divisible_by_3:
                res.append("Fizz")
            elif divisible_by_5:
                res.append("Buzz")
            else:
                res.append(str(n))
        return res


class Solution2:
    def fizz_buzz(self, n: int) -> list:
        return [self._fizz_buzz_helper_v3(i) for i in range(1, n + 1)]

    def _fizz_buzz_helper(self, n: int) -> str:
        """
        解法二：字符串操作（拼接）

        :param n: int, an integer
        :return: str, the corresponding string representation of the integer
        """
        # return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)
        return "Fizz" * (not n % 3) + "Buzz" * (not n % 5) or str(n)

    def _fizz_buzz_helper_v2(self, n: int) -> str:
        """
        解法二：字符串操作（切片）

        :param n: int, an integer
        :return: str, the corresponding string representation of the integer
        """
        return "FizzBuzz"[(n % 3 > 0) * 4:(n % 5 < 1) * 4 + 4] or str(n)

    def _fizz_buzz_helper_v3(self, n: int) -> str:
        """
        解法二：字符串操作（切片）

        :param n: int, an integer
        :return: str, the corresponding string representation of the integer
        """
        return "FizzBuzz"[n%-3&-4:n%-5&8^12] or str(n)


class Solution3:
    def fizz_buzz(self, n: int) -> list:
        """
        解法三：字符串操作（拼接），提升扩展性
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param n: int, an integer
        :return: str, the corresponding string representation of the integer
        """
        res = []
        fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1, n + 1):
            out_str = ""
            for k in fizz_buzz_dict.keys():
                if i % k == 0:
                    out_str += fizz_buzz_dict[k]
            if out_str:
                res.append(out_str)
            else:
                res.append(str(i))
        return res


if __name__ == '__main__':
    solution = Solution2()
    print(solution.fizz_buzz(15))
