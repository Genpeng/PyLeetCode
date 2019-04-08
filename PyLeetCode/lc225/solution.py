# _*_ coding: utf-8 _*_

"""
This is the solution of no. 225 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/implement-stack-using-queues/

The description of problem is as follow:
==========================================================================================================
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
- You must use only standard operations of a queue -- which means only push to back,
  peek/pop from front, size, and is empty operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by
  using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations
  will be called on an empty stack).
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/08
"""

from collections import deque


class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q1, self._q2, self._top = deque(), deque(), None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._top = x
        self._q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        if len(self._q1) == 1:
            ret = self._q1.popleft()
            self._top = None
        else:
            while len(self._q1) > 1:
                self._top = self._q1.popleft()
                self._q2.append(self._top)
            ret = self._q1.popleft()
            self._q1, self._q2 = self._q2, self._q1
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        return self._top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._q1


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q1, self._q2 = deque(), deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._q2.append(x)
        while not self.empty():
            self._q2.append(self._q1.popleft())
        self._q1, self._q2 = self._q2, self._q1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        return self._q1.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        return self._q1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._q1


class MyStack3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._q.append(x)
        for i in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        return self._q.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The stack is empty!!!")
        return self._q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._q


def main():
    my_stack = MyStack3()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.top())


if __name__ == '__main__':
    main()
