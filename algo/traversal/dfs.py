from __future__ import annotations
from typing import List, Tuple

class DepthFirstSearch:
    class Counter:
        def __init__(self) -> None:
            self.counter = 0
            
        def retrieve(self) -> int:
            self.counter += 1
            return self.counter
    
    
    @classmethod
    def search(cls, array: List[List[int]]) -> List[List[int]]:
        output = [None] * len(array)
        counter = DepthFirstSearch.Counter()
        
        for i in range(len(output)):
            output[i] = [0] * len(array[0])
            
        DepthFirstSearch.dfs(output, (0, 0), counter)
            
        return output
    
    
    @classmethod
    def dfs(cls, array: List[List[int]], pos: Tuple[int, int], counter: DepthFirstSearch.Counter) -> None:
        row = pos[0]
        col = pos[1]
        
        if (row >= 0 and row < len(array)) and (col >= 0 and col < len(array[0])) and array[row][col] <= 0:
            array[row][col] = counter.retrieve()
            
            DepthFirstSearch.dfs(array, (row + 1, col), counter)
            DepthFirstSearch.dfs(array, (row - 1, col), counter)
            DepthFirstSearch.dfs(array, (row, col + 1), counter)
            DepthFirstSearch.dfs(array, (row, col - 1), counter)
            

if __name__ == "__main__":
    pass