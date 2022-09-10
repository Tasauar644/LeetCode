from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0
        
        while left < right:
            
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
                
        return result
        
        
S = Solution()
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        