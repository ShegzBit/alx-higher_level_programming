#!/usr/bin/python3
"""A module for singly linked list in python"""


class Node:
    """A singly linked list node class"""
    def __init__(self, data, next_node=None):
        """Node initializer"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns value stored in data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list class"""
    def __init__(self):
        """slinkedlist init function"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node in the right position ascendingly"""
        temp = Node(value)
        head2 = self.__head
        prev = None
        if self.__head is None:
            self.__head = temp
            return
        prev = None
        while head2 is not None and head2.data < temp.data:
            prev = head2
            head2 = head2.next_node

        if prev is None:
            temp.next_node = self.__head
            self.__head = temp
        elif head2 is None:
            prev.next_node = temp
        else:
            temp.next_node = head2
            prev.next_node = temp

    def __str__(self):
        """Manage printing using print functions"""
        my_list = list()
        temp = self.__head
        while temp is not None:
            if temp.next_node is not None:
                my_list.append(f"{temp.data}\n")
            else:
                my_list.append(f"{temp.data}")
            temp = temp.next_node
        return "".join(my_list)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
