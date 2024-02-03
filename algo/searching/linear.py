from __future__ import annotations
from typing import List

class LinearSearch:
    @classmethod
    def linear_search(cls, arr: List[int], elem: int) -> int:
        for i in range(len(arr)):
            if arr[i] == elem:
                return i
            
        return -1

if __name__ == "__main__":
    pass