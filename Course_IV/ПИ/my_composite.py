from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Node(ABC):

    @property
    def parent(self) -> Node:
        return self._parent

    @parent.setter
    def parent(self, parent: Node):
        self._parent = parent

    def add(self, node: Node) -> None:
        pass

    def remove(self, node: Node) -> None:
        pass

    def is_box(self) -> bool:
        return False

    @abstractmethod
    def summ(self) -> str:
        pass

class ItemNode(Node):

    def __init__(self, price) -> None:
        super().__init__()
        self.price = price

    def summ(self) -> float:
        return self.price

class BoxNode(Node):

    def __init__(self) -> None:
        self._children: List[Node] = []

    def add(self, node: Node) -> None:
        self._children.append(node)
        node.parent = self

    def remove(self, node: Node) -> None:
        self._children.remove(node)
        node.parent = None

    def is_box(self) -> bool:
        return True

    def summ(self) -> float:
        result = 0
        for child in self._children:
            result += child.summ()
        return result

if __name__ == "__main__":
    tree = BoxNode()

    box1 = BoxNode()
    box1.add(ItemNode(20))
    box1.add(ItemNode(30))

    box2 = BoxNode()
    box2.add(ItemNode(50))

    tree.add(box1)
    tree.add(box2)
    tree.add(ItemNode(150))

    print(tree.summ())