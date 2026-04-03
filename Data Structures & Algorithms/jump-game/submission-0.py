class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        #start = goal
        test = goal - 1
        jump = 1
        while goal > -1 and test > -1:    
            if test > -1:
                if nums[test] >= jump:
                    goal = test
                    test = goal - 1
                    jump = 1
                else:
                    test -= 1
                    jump += 1
        
        if goal == 0:
            return True
        else:
            return False
        