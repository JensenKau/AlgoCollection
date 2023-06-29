from __future__ import annotations
from typing import List, Tuple
from math import inf

class Graph:
    def __init__(self, connections: List[Tuple[int, int, int]], start: int, end: int) -> None:
        self.vertices = self.build_graph(connections)
        self.start = self.vertices[start]
        self.end = self.vertices[end]
            
            
    def build_graph(self, connections: List[Tuple[int, int, int]]) -> List[Node]:
        vertices = None
        max_value = 0
        
        for connection in connections:
            max_value = max(max_value, connection[0], connection[1])
            
        vertices = [None] * (max_value + 1)
        
        for connection in connections:
            if vertices[connection[0]] is None:
                vertices[connection[0]] = Node(connection[0])
            if vertices[connection[1]] is None:
                vertices[connection[1]] = Node(connection[1])
                
            vertices[connection[0]].edges.append(Edge(vertices[connection[0]], vertices[connection[1]], connection[2]))
            
        return vertices
    
    
class Node:
    def __init__(self, id: int) -> None:
        self.id = id
        self.index = id + 1
        self.distance = inf
        self.edges = []
    
    
class Edge:
    def __init__(self, start: Node, end: Node, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight
    
    
class MinHeap:
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes
        self.heap = [None] * (len(nodes) + 1)
        self.last = len(self.heap) - 1
        
        for i in range(len(nodes)):
            self.heap[i + 1] = self.nodes[i]
        
        
    def __swap(self, index1: int, index2: int) -> None:
        self.heap[index1].index = index2
        self.heap[index2].index = index1
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
        
    def __smaller_child(self, index: int) -> int:
        if index * 2 + 1 <= self.last:
            if self.heap[index * 2].distance <= self.heap[index * 2 + 1].distance:
                return index * 2
            else:
                return index * 2 + 1
        else:
            return index * 2
        
    
    def __sink(self, index: int) -> None:
        while index * 2 <= self.last:
            smaller_index = self.__smaller_child(index)
            
            if self.heap[index].distance > self.heap[smaller_index].distance:
                self.__swap(index, smaller_index)
                index = smaller_index
            else:
                break
            
    
    def __rise(self, index: int) -> None:
        while index > 1:
            if self.heap[index].distance < self.heap[index // 2].distance:
                self.__swap(index, index // 2)
                index = index // 2
            else:
                break
            
    
    def __len__(self) -> int:
        return self.last
    
    
    def pop(self) -> Node:
        output = self.heap[1]
        
        self.__swap(1, self.last)
        self.last -= 1
        self.__sink(1)
        
        return output
    
    
    def update(self, node: Node) -> None:
        self.__rise(node.index)
    
    
class Dijkstra:
    @classmethod
    def shortest_distance(cls, locations: List[Tuple[int, int, int]], start: int, end: int) -> int:
        graph = Graph(locations, start, end)
        heap = MinHeap(graph.vertices)
        
        starting_location = graph.start
        starting_location.distance = 0
        heap.update(starting_location)
        
        while len(heap) > 0:
            current_location = heap.pop()
            
            if current_location.id == end:
                return current_location.distance
            
            for edge in current_location.edges:
                edge.end.distance = min(edge.end.distance, current_location.distance + edge.weight)
                heap.update(edge.end)
                
        return -1
    
    
if __name__ == "__main__":
    pass