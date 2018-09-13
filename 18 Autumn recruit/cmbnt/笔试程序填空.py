# 两个栈实现一个队列

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if not self.stack1:
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ret
