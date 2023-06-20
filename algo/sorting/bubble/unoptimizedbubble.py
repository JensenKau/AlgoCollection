from __future__ import annotations
from typing import List

class UnoptimizedBubbleSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    
    
if __name__ == "__main__":
    pass