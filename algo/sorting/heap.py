from __future__ import annotations
from typing import List

class HeapSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        def sink(index: int, pointer: int) -> None:
            while index * 2 + 1 < pointer:
                bigger_index = bigger_child(index, pointer)
                
                if array[index] < array[bigger_index]:
                    array[index], array[bigger_index] = array[bigger_index], array[index]
                    index = bigger_index
                else:
                    break
        
        
        def bigger_child(index: int, pointer: int) -> int:
            if index * 2 + 2 < pointer:
                if array[index * 2 + 1] > array[index * 2 + 2]:
                    return index * 2 + 1
                else:
                    return index * 2 + 2
            else:
                return index * 2 + 1
        
        
        HeapSort.heapify(array)
        
        pointer = len(array)
        
        while pointer > 0:
            pointer -= 1
            array[0], array[pointer] = array[pointer], array[0]
            sink(0, pointer)
    
    
    @classmethod
    def heapify(cls, array: List[int | float]) -> None:
        def bigger_child(index: int) -> int:
            if index * 2 + 2 < len(array):
                if array[index * 2 + 1] > array[index * 2 + 2]:
                    return index * 2 + 1
                else:
                    return index * 2 + 2
            else:
                return index * 2 + 1
        
        
        def sink(index: int) -> None:
            while index * 2 + 1 < len(array):
                bigger_index = bigger_child(index)
                
                if array[index] < array[bigger_index]:
                    array[index], array[bigger_index] = array[bigger_index], array[index]
                    index = bigger_index
                else:
                    break
                
        for i in range((len(array) // 2) - 1, -1, -1):
            sink(i)


if __name__ == "__main__":
    import random
    
    arr = [random.randint(1,10000) for i in range(100)]
    
    print(arr)
    
    HeapSort.sort(arr)
    
    print(arr)