class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        choice = nums[0]

        count = 1

        for i in range(1, len(nums)):
            if nums[i] == choice:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                choice = nums[i]
                count = 1
        
        return choice