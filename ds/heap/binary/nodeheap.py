from __future__ import annotations
from typing import List, Any
from collections import deque

class Node:
    def __init__(self, item: Any) -> None:
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.previous = None
        self.next = None

class NodeHeap:
    def __init__(self, array: List[int]) -> None:
        self.root = None
        self.size = 0
        self.last = None
        
        self.__heapify(array)
        
        
    def __heapify(self, array: List[int]) -> None:
        def smaller_child(index: int, array: List[int]) -> int:
            if index * 2 + 1 < len(array):
                if array[index * 2 + 1] < array[index * 2]:
                    return index * 2 + 1
                else:
                    return index * 2
            else:
                return index * 2
        
        
        def sink(index: int, array: List[int]) -> None:
            while index * 2 < len(array):
                smaller_index = smaller_child(index, array)
                
                if array[index] < array[smaller_index]:
                    array[index], array[smaller_index] = array[smaller_index], array[index]
                    index = smaller_index
                else:
                    break
        
        
        temp = [None] * (len(array) + 1)
        
        for i in range(len(array)):
            temp[i + 1] = array[i]
            
        for i in range(len(temp) // 2, 0, -1):
            sink(i)
            
        for i in range(1, len(temp)):
            temp[i] = Node(temp[i])
            
        for i in range(1, len(temp)):
            if i * 2 < len(temp):
                temp[i].left = temp[i * 2]
                temp[i * 2].parent = temp[i]
            if i * 2 + 1 < len(temp):
                temp[i].right = temp[i * 2 + 1]
                temp[i * 2 + 1].parent = temp[i]
                
            if i + 1 < len(temp):
                temp[i].next = temp[i + 1]
                
            temp[i].previous = temp[i - 1]
                
        self.root = temp[1] if len(temp) > 1 else None
        self.last = temp[-1] if self.root is not None else None
        self.size = len(array)
    
    
    def __rise(self, node: Node) -> None:
        while node.parent is not None:
            if node.item < node.parent.item:
                node.item, node.parent.item = node.parent.item, node.item
                node = node.parent
            else:
                break
    
    
    def __sink(self, node: Node) -> None:
        while node.left is not None:
            smaller_node = self.__smaller_node(node)
            
            if node.item > smaller_node.item:
                node.item, smaller_node.item = smaller_node.item, node.item
                node = smaller_node
            else:
                break
    
    
    def __smaller_node(self, node: Node) -> Node:
        if node.right is not None:
            if node.item.left <= node.item.right:
                return node.left
            else:
                return node.right
        else:
            return node.left
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    
    def insert(self, num: int) -> None:
        node = Node(num)
        node.previous = self.last
        self.last.next = node
        self.last = node
        
        if node.previous is None:
            self.root = node
        if node.previous is self.root:
            node.previous.left = node
            node.parent = node.previous
        else:
            if node.previous.parent.right is None:
                node.previous.parent.right = node
                node.parent = node.previous.parent
            else:
                node.previous.parent.next.left = node
                node.parent = node.previous.parent.next
        
        self.size += 1
        
        self.__rise(node)
    
    
    def pop(self) -> int:
        if self.size == 0:
            raise ValueError("Heap is empty")
        
        output = self.root.item
        last_node = self.last
        
        last_node.previous.next = None
        
        if last_node.parent.right is last_node:
            last_node.parent.right = None
        else:
            last_node.parent.left = None
            
        self.size -= 1
        
        self.__sink(self.root)
        
        return output
    
    
    def peek(self) -> int:
        if self.size == 0:
            raise ValueError("Heap is empty")
        
        return self.root.item
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        queue = deque()
        
        queue.append(self.root)
        
        i = 0
        while len(queue) > 0:
            node = queue.popleft()
            temp[i] = node.item
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
            i += 1
            
        return f"[{', '.join(temp)}]"
            
    
    
if __name__ == "__main__":
    pass