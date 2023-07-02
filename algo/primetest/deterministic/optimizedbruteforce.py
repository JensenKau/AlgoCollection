from __future__ import annotations
from math import sqrt

class OptimizedBruteForce:
    
    @classmethod
    def is_prime(cls, num: int) -> bool:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                return False 
            
        return True
    

if __name__ == "__main__":
    pass