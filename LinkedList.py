##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	LinkedList.py
# @version	1
# @author	Kiran S | R&D Manager | Nokia
# @short	LinkedList implementation
# LinkedList implementation using Nodes
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################

'''Linked List Implementation'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, firstNode: Node = None) -> None:
        self.firstNode = firstNode

    def search(self, value):
        currentNode = self.firstNode
        currentIndex = 0

        while currentNode:
            if currentNode.data == value:
                return currentIndex
            else:
                currentNode = currentNode.next
                currentIndex+=1

        return None    

    def printLinkedList(self):
        currentNode = self.firstNode

        while currentNode:
            print(currentNode.data + '->',end='')
            currentNode = currentNode.next

        print("None")        

    def read(self, index: int):
        currentNode = self.firstNode
        currentIndex = 0

        while currentIndex < index:
            if currentNode:
                currentNode = currentNode.next
                currentIndex+=1
            else:
                return None
        
        return currentNode

    def insert(self, node: Node, index):
        if self.firstNode == None:
            self.firstNode = node
            return True

        currentNode = self.firstNode
        currentIndex = 0

        while currentIndex < (index - 1):
            if currentNode:
                currentNode = currentNode.next
                currentIndex+=1
            else:
                return False

        node.next = currentNode.next
        currentNode.next = node

        return True

    def delete(self, index):
        if self.firstNode == None:
            return False
        
        if index == 0:
            self.firstNode = self.firstNode.next
            return True

        currentNode = self.firstNode
        currentIndex = 0

        while currentIndex < (index - 1):
            if currentNode:
                currentNode = currentNode.next
                currentIndex+=1
            else:
                return False

        nodeToBeDeleted: Node = currentNode.next    
        currentNode.next = nodeToBeDeleted.next
        return True

    
#Test
node_1 = Node("Once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

list_1 = LinkedList(node_1)
list_1.insert(node_2,1)
list_1.insert(node_3,2)
list_1.insert(node_4,3)

list_1.printLinkedList()




        
        