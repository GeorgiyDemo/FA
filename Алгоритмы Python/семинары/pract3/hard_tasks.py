"""
Разбор односвязанных списков по заданиям 13-
"""

def print_backward(lst):
    if lst == None:
        return
    head = lst
    tail = lst.next
    print_backward(tail)
    print(head)

def print_list(node):
    while node:
        print(node)
        node = node.next
    print

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4

print("Узел 1")
print_list(node1)
print_backward(node1)

print("Узел 2")
print_list(node2)
print_backward(node2)

print("Узел 3")
print_list(node3)
print_backward(node3)

print("Узел 4")
print_list(node4)
print_backward(node4)