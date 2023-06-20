from __future__ import annotations
from typing import List

class SelectionSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        for i in range(len(array)):
            index = i
            
            for j in range(i + 1, len(array)):
                if array[j] < array[index]:
                    index = j
                    
            array[i], array[index] = array[index], array[i]
    
    
if __name__ == "__main__":
    pass