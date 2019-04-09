# _*_ coding: utf-8 _*_

"""
This is the solution of no. 232 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/implement-queue-using-stacks/

The description of problem is as follow:
==========================================================================================================
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
- You must use only standard operations of a stack -- which means only push to top,
  peek/pop from top, size, and is empty operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate a stack by
  using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek operations
  will be called on an empty queue).
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/09
"""


class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._s1, self._s2 = [], []

    def push(self, e):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self._s1:
            self._s2.append(self._s1.pop())
        self._s1.append(e)
        while self._s2:
            self._s1.append(self._s2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            raise Exception("[ERROR] The queue is empty!!!")
        return self._s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            raise Exception("[ERROR] The queue is empty!!!")
        return self._s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self._s1


class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in_stack, self._out_stack, self._front = [], [], None

    def push(self, e):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self._in_stack:
            self._front = e
        self._in_stack.append(e)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The queue is empty!!!")
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
        return self._out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            raise Exception("[ERROR] The queue is empty!!!")
        if self._out_stack:
            return self._out_stack[-1]
        else:
            return self._front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self._in_stack) and (not self._out_stack)


def main():
    my_queue = MyQueue2()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.pop())


if __name__ == '__main__':
    main()
