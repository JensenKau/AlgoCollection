from __future__ import annotations
from typing import List

class BubbleSort:
    
    @classmethod
    def sort(self, array: List[int | float]) -> None:
        for i in range(1, len(array)):
            for j in range(i - 1, -1, -1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                else:
                    break
    
    
if __name__ == "__main__":
    pass