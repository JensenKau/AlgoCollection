from __future__ import annotations
from typing import List

class MedianOfMedian:
    
    @classmethod
    def choose_pivot(cls, array: List[int]) -> int:
        return MedianOfMedian.choose_pivot_aux(array, 0, len(array) - 1)
    
    @classmethod
    def choose_pivot_aux(cls, array: List[int], start: int, end: int) -> int:
        if (end - start + 1) <= 5:
            return MedianOfMedian.median_five_aux(array, start, end)
        else:
            medians = None
            med_pointer = 0
            
            five = [0] * 5
            pointer = 0
            
            if (end - start + 1) % 5 == 0:
                medians = [0] * ((end - start + 1) // 5)
            else:
                medians = [0] * (((end - start + 1) // 5) + 1)
                                
            for i in range(start, end + 1):
                five[pointer] = array[i]
                pointer += 1
                
                if pointer == 5:
                    medians[med_pointer] = MedianOfMedian.median_five(five)
                    med_pointer += 1
                    pointer = 0
                    
                elif i == end:
                    temp = [0] * pointer
                    
                    for i in range(len(temp)):
                        temp[i] = five[i]
                        
                    medians[med_pointer] = MedianOfMedian.median_five(temp)
                                                                                                    
            return MedianOfMedian.quickselect(medians, len(medians) // 2, 0, len(medians) - 1)
    
    
    @classmethod
    def median_five(cls, array: List[int]) -> int:
        return MedianOfMedian.median_five_aux(array, 0, len(array) - 1)
    
    @classmethod
    def median_five_aux(cls, array: List[int], start: int, end: int) -> int:        
        for i in range(start + 1, end + 1):
            current = array[i]
            
            for j in range(i - 1, start - 1, -1):
                if array[j] > current:
                    array[j + 1] = array[j]
                else:
                    array[j + 1] = current
                    break
                
                if j == start:
                    array[j] = current
                                                
        return array[(start + end + 1) // 2]
    
    
    @classmethod
    def quickselect(cls, array: List[int], k: int, start: int, end: int) -> int:
        pivot = MedianOfMedian.choose_pivot_aux(array, start, end)
        point = MedianOfMedian.partition(array, start, end, pivot)        
                
        if point == k:
            return array[point]
        elif k < point:
            return MedianOfMedian.quickselect(array, k, start, point - 1)
        else:
            return MedianOfMedian.quickselect(array, k, point + 1, end)
        
    
    @classmethod
    def partition(cls, array: List[int], start: int, end: int, pivot: int) -> int:
        pointer = start - 1
        
        if array[end] != pivot:
            for i in range(start, end + 1):
                if array[i] == pivot:
                    array[i], array[end] = array[end], array[i]
        
        for i in range(start, end + 1):
            if array[i] <= pivot:
                pointer += 1
                array[i], array[pointer] = array[pointer], array[i]
                                
        return pointer
    
    
if __name__ == "__main__":
    pass