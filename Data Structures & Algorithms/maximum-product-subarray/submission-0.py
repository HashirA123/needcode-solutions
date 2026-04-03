class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Actually a DP problem, can be sliding window but that hard

        # use min and max values

        res = max(nums) # res is just set to the max value

        current_max, current_min = 1, 1

        for n in nums:
            if n == 0:
                current_max, current_min = 1, 1
                continue
            temp = current_max
            current_max = max(n * current_max, # n * current_max gives larger num if n is +
                                n * current_min, # n * current_min gives larger num if both are -
                                n)    # n is just bigger than both options
            # same with current_min, but get the smallest of the three
            current_min = min(n * temp, # n * current_max gives larger num if n is +
                                n * current_min, # n * current_min gives larger num if both are -
                                n)    # n is just bigger than both options)
            
            res = max(res, current_max)
        
        return res

            
