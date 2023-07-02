from __future__ import annotations

class BruteForce:
    
    @classmethod
    def is_prime(cls, num: int) -> bool:
        for i in range(2, num):
            if num % i == 0:
                return False 
            
        return True
    

if __name__ == "__main__":
    pass