class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix arrays??

        prefix = [1] * (len(nums)+1)
        # [1, 1,  1,  2, 8] # product coming before not including itself
        postfix = [1] * (len(nums)+1)
        #    [48, 24, 6, 1, 1] # product coming after not includinf itself

        i, j = 0, len(nums)-1
        while i < len(nums):
            prefix[i+1] = prefix[i] * (nums[i-1] if i > 0 else 1)
            postfix[j] = postfix[j+1] * (nums[j+1] if j < len(nums)-1 else 1)
            i += 1
            j -= 1
            
        res = []
        i = 1
        while i < len(prefix):
            res.append(prefix[i] * postfix[i-1])
            i += 1
        
        return res