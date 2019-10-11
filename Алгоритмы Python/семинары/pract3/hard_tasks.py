"""
Разбор двусвязных списков по заданиям 13-14
"""
def print_backward(lst):
    if lst == None:
        return
    head = lst
    tail = lst.next
    print_backward(tail)
    print(head, head.previous)

class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next  = next
        self.previous = previous

    def __str__(self):
        return str(self.value)

def main():
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.previous = node1

    node3 = Node(3)
    node2.next = node3
    node3.previous = node2

    node4 = Node(4)
    node3.next = node4
    node4.previous = node3

    print("Узел 1")
    print_backward(node1)

    print("Узел 2")
    print_backward(node2)

    print("Узел 3")
    print_backward(node3)

    print("Узел 4")
    print_backward(node4)

if __name__ == "__main__":
    main()