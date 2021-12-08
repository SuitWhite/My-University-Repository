import random
from valid import *
from IterGener import *


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class MyLinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def get_head(self):
        return self._head

    def get_size(self):
        return self._size

    def push_back(self, val):
        if self._head is None:
            self._head = Node(val)
        else:
            current_node = self._head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = Node(val)
        self._size = self._size + 1

    def randomize_elements(self, number, left, right):
        if self._head is None:
            index = 0
            while index != number:
                element = random.randrange(left, right + 1)
                self.push_back(element)
                index = index + 1
        else:
            current_size = self._size
            while self._size != current_size + number:
                element = random.randrange(left, right + 1)
                self.push_back(element)

    def input_keyboard(self, num):
        if self._head is None:
            index = 0
            while index != num:
                element = input_check_list_element_or_interval_limit()
                self.push_back(element)
                index = index + 1
        else:
            current_size = self._size
            while self._size != current_size + num:
                element = input_check_list_element_or_interval_limit()
                self.push_back(element)

    def new_node(self, value, index):
        if index == 0:
            new_node = Node(value)
            temp = self._head
            self._head = new_node
            new_node.next_node = temp
        elif index > 0:
            previous = self._head
            for i in range(index - 1):
                previous = previous.next_node
            new_element = Node(value)
            new_element.next_node = previous.next_node
            previous.next_node = new_element
        self._size = self._size + 1

    def delete_node(self, index):
        if self._head is None:
            print("You can't delete node, because your list is empty")
        else:
            if index == 0:
                self._head = self._head.next_node
            elif index > 0:
                previous = self._head
                for i in range(index - 1):
                    previous = previous.next_node
                element_to_delete = previous.next_node
                previous.next_node = element_to_delete.next_node
            self._size = self._size - 1

    def exercise_count(self):
        current = self._head
        tmp = 1
        while current is not None:
            if current.value > 0:
                result = tmp
            tmp *= current.value
            current = current.next_node
        return result

    def print_list(self):
        current = self._head
        for i in range(self._size):
            print(current.value, end=' ')
            current = current.next_node
        print()

    def extend(self, iterable):
        for elem in iterable:
            self.push_back(elem)