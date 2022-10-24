#!usr/bin/python3
"""Class for the Node Structure"""


class Node:
    """Represents a Node in a singly linked list
    Attributes:
        __data (int): integer in the singly linked list
        __next_node (Node): next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """Creates an object of attribute size
        Args:
            data (int): integer data of list Node
            next_node (Node): next node in the linked list
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of __data
        Returns:
            The integer of a linked list
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data
        Args:
            value (int): value in linked list
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for __position
        Returns:
            pointer to the next node in linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __position
        Args:
            value (Node): pointer to the next node
        Returns:
            None
        """
        if (value is not None or
                type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Class to form the SinglyLinkedList"""


class SinglyLinkedList:
    """Represents a Node Structure
        Attributes:
        """

    def __init__(self):
        """Creates a class to represent linked list
                Args:
                Returns: None
                """
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the SinglyLinkedList
        The node is inserted into the list at the
        correct ordered numerical position.
        Args:
            value (Node): The new node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp_node = self.__head
            while (tmp_node.next_node is not None and
                   tmp_node.data < value):
                tmp_node = tmp_node.next_node
            new.next_node = tmp_node.next_node
            tmp_node.next_node = new

    def __str__(self):
        """Define the print() representation of a Singly Linked List"""
        values = []
        tmp_node = self.__head
        while tmp_node is not None:
            values.append(str(tmp_node.data))
            tmp_node = tmp_node.next_node
        return ('\n'.join(values))
