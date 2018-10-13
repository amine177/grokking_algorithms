# !/bin/env python3
# -*- coding: utf-8 -*-

import random


class Node:
    """A class representing a node in a linked list"""

    def __init__(self, value, next):
        """Node(value, next)
        Arguments:
            value: the value
            next: the next node
        """

        self.value = value
        self.next = next


class Queue:
    """A class representing a FIFO queue"""

    def __init__(self, max):
        """Queue(max)
        Arguments:
            max: the queue's capacity
        """

        self.max = max
        self.number = 0
        self.list = None

    def __find(self, l, v):
        """internal"""

        if l.value == v:
            return True
        elif l.next is None:
            return False
        else:
            return self.__find(l.next, v)

    def find(self, v):
        """find a value in the queue
        Arguments:
            v: value
        """
        return self.find(self.list, v)

    def push(self, value):
        """pushes a value to the queue
        Arguments:
            value: the value to push
        """

        if self.list is None:
            self.list = Node(value, None)
        else:
            if self.number + 1 > self.max:
                raise Exception("queue is full")
            n = self.list
            while (n.next is not None):
                n = n.next
            n.next = Node(value, None)
        self.number += 1

    def pop(self):
        """popes a value from the queue
        Arguments:
            None
        """

        if self.number == 0:
            return None

        n = self.list
        self.list = self.list.next
        self.number -= 1
        return n.value

    def isempty(self):
        """returns True if the queue is empty false otherwise"""
        return self.number == 0

    def isfull(self):
        """returns True if the queue is full, Fasle otherwise"""
        return self.number == self.max

    def __len__(self):
        """returns the number of elements in the queue"""
        return self.number


if __name__ == "__main__":

    q = Queue(300)
    while not q.isfull():
        q.push(random.random() * 5)
    while not q.isempty():
        print("q.pop() = {}".format(q.pop()))
