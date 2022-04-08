##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	BinarySearchTree.py
# @version	1
# @author	Kiran S | R&D Manager
# @short	BinarySearchTree implementation
# BinarySearchTree implementation
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################

"""A Binary Search Tree Implementation"""

class TreeNode:
    def __init__(self, data, leftChild = None, rightChild = None) -> None:
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
        
class BinarySearchTree:
    rootNode: TreeNode

    def __init__(self, node: TreeNode = None) -> None:
        self.rootNode = node

    #search for a node
    def search(self, data, node: TreeNode = None, searchFromRoot = True):
        #setup search from root
        if searchFromRoot:
            currentNode = self.rootNode
        else:
            currentNode = node

        #base case
        if currentNode is None or currentNode.data == data:
            return currentNode

        if data < currentNode.data:
            return self.search(data, currentNode.leftChild, False)
        elif data > currentNode.data:
            return self.search(data, currentNode.rightChild, False)

    #insert nodes
    def insert(self, data, node: TreeNode = None, searchFromRoot = True):
        #setup search from root
        if searchFromRoot:
            currentNode = self.rootNode
        else:
            currentNode = node

        #for inserting into an empty BST
        if self.rootNode is None:
            self.rootNode = TreeNode(data)
            return True

        #for inserting into an existing BST
        if data <= currentNode.data:
            if currentNode.leftChild is None:
                currentNode.leftChild = TreeNode(data)
            else:
                self.insert(data, currentNode.leftChild, False)
        else:
            if currentNode.rightChild is None:
                currentNode.rightChild = TreeNode(data)
            else:
                self.insert(data, currentNode.rightChild, False)

        return True
        
#Test
#node_1 = TreeNode(10)
#node_2 = TreeNode(40)
#node_3 = TreeNode(20, node_1,node_2)

tree = BinarySearchTree()
tree.insert(20)
tree.insert(40)
tree.insert(10)

findNode: TreeNode = tree.search(40)
print(findNode.data if findNode else None)



