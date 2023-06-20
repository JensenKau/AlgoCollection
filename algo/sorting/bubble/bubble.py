from __future__ import annotations
from typing import List

class BubbleSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        for i in range(len(array) - 1, 0, -1):
            swapped = False
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
                    
            if not swapped:
                break
    
    
if __name__ == "__main__":
    pass