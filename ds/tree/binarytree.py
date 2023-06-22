from __future__ import annotations
from typing import List, Any

class BinaryTree:
    class TreeNode:
        def __init__(self, item: Any = None, left: BinaryTree.TreeNode = None, right: BinaryTree.TreeNode = None) -> None:
            self.item = item
            self.left = left
            self.right = right
            
            
    def __init__(self, array: List[int | None]) -> None:
        self.root = self.build(array)
    
    
    def build(self, array: List[int | None]) -> BinaryTree.TreeNode:
        nodes = [None] * (len(array) + 1)
        
        for i in range(len(array)):
            if array[i] is not None:
                nodes[i + 1] = BinaryTree.TreeNode(array[i])
                
        for i in range(1, len(nodes) // 2):
            if nodes[i] is not None:
                if i * 2 < len(nodes) and nodes[i * 2] is not None:
                    nodes[i].left = nodes[i * 2]
                if i * 2 + 1 < len(nodes) and nodes[i * 2 + 1] is not None:
                    nodes[i].right = nodes[i * 2 + 1]
                    
        return nodes[1]
    

if __name__ == "__main__":
    pass