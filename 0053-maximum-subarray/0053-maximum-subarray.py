class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        tsum = nums[0]
        for i in nums[1:]:
            sum += i
            if sum < i :
                
                sum = i
            
            tsum = max(sum,tsum)

        return tsum 

        