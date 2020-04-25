from .LinkedListNode import *

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add a new data to tail of list
    def append(self, data):
        newNode = LinkedListNode(data)

        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.size += 1

    def find(self, data):
        # If the the list is empty
        if self.head == None:
            return None

        currentNode = self.head

        while currentNode:
            if currentNode.data == data:
                return currentNode
            currentNode = currentNode.next

        return None
