from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
    def helper(self,nums):
        rob1, rob2 = 0, 0
        
        for i in nums:
            newRob = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
        
S = Solution()
print(S.rob([1,2,3,1]))