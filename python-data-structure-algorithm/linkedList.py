# Sequential, shuld hae ref to next node
#consumes memory
# nodes to be read in order from the beginning
# Array item can be reached via indexes in O(1) time
# Difficulty in reverse traversing
#Singly lined lists are difficult to navigate backwards
#Solution - Doubly linked lists are easier to rad but memory is wasted

# Python program to delete a node from linked list 
  
# Node class  
class Node:
    def __init__(self, cargo=None, next=None):
        print(self)
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

node = Node("AS")
    print(node)