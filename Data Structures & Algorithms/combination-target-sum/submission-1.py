class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currentList, currentSum):
            if currentSum == target:
                res.append(currentList.copy()) # make sure to use .copy()
                return
            if i >= len(nums):
                return
            
            for index in range(i, len(nums)):
                # if adding this number makes it bigger than target
                # ignore
                if currentSum + nums[index] > target:
                    continue
                currentList.append(nums[index])
                dfs(index, currentList, currentSum+nums[index])
                currentList.pop()
            
            return
        
        dfs(0, [], 0)
        return res