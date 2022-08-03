from typing import List
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(math.sqrt(c))
        while a<=b:
            if a*a+b*b==c:
                return True
            elif a*a+b*b<c:
                a+=1
            else:
                b-=1
        return False
        
        
        
        

S = Solution()
print(S.judgeSquareSum(5))