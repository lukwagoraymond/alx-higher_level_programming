#!/usr/bin/python3
"""Class for Singly Linked Lists Data Structure"""


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the Linked List
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Add a New_node at the beginning
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval is not None:
            laste = laste.nextval
        laste.nextval = NewNode

    # Function to Add Node inbetween two Nodes
    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        Newnode = Node(newdata)
        Newnode.nextval = middle_node.nextval
        middle_node.nextval = Newnode

    # Function to Remove Node by Name
    def RemoveNode(self, Removekey):
        Headval = self.headval

        if Headval is not None:
            if Headval.dataval == Removekey:
                self.headval = Headval.nextval
                Headval = None
                return
        while Headval is not None:
            if Headval.dataval == Removekey:
                break
            prev = Headval
            Headval = Headval.nextval

        if Headval is None:
            return

        prev.nextval = Headval.nextval
        Headval = None


list1 = SLinkedList()
#list1.headval = Node('Monday')
#e2 = Node('Tuesday')
#e3 = Node('Wednesday')

# List first Node to second Node
#list1.headval.nextval = e2

# List second Node to Third Node
#e2.nextval = e3

list1.AtBeginning('Sun')
list1.AtBeginning('Mon')
list1.AtBeginning('Tue')
list1.AtBeginning('Wed')
list1.AtEnd('Thurs')
list1.Inbetween(list1.headval.nextval, "Saturday")
list1.RemoveNode('Tue')
list1.listprint()
