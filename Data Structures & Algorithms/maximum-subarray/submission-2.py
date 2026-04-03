class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # more like a sliding window question
        # increase the window as long as total
        # is positive, reduce window from start
        # if sum/counter ever dips below zero.
        # check for max at each size increase.
        
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