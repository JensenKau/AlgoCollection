from __future__ import annotations
from typing import List, Tuple

class Graph:
    def __init__(self, connections: List[Tuple[int, int, int]]) -> None:
        self.vertices = self.build_graph(connections)
        
        
    def build_graph(self, connections: List[Tuple[int, int, int]]) -> List[Vertex]:
        vertices = None
        max_value = 0
        
        for connection in connections:
            max_value = max(max_value, connection[0], connection[1])
            
        vertices = [None] * (max_value + 1)
        
        for connection in connections:
            if vertices[connection[0]] is None:
                vertices[connection[0]] = Vertex(connection[0])
                
            if vertices[connection[1]] is None:
                vertices[connection[1]] = Vertex(connection[1])
                
            vertices[connection[0]].edges.append(Edge(vertices[connection[0]], vertices[connection[1]], connection[2]))
            
        return vertices


class Vertex:
    def __init__(self, id: int) -> None:
        self.id = id
        self.edges = []


class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight
        

if __name__ == "__main__":
    pass