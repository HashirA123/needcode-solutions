class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf

        counter = 0

        start = 0
        end = 0

        while end < len(nums):
            right = nums[end]
            counter += right

            maxSum = max(counter, maxSum)

            while counter < 0 and start <= end:
                left = nums[start]
                counter -= left
                start += 1
            
            end += 1
        
        return maxSum