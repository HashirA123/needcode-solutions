class Solution:
    def rob(self, nums: List[int]) -> int:
        # break down into base problem
        store = {}

        def helper(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if (i, flag) in store:
                return store[(i, flag)]

            store[(i, flag)] = max(nums[i] + helper(i+2, flag or (i==0)), helper(i+1, flag))

            return store[(i, flag)]

        return max(helper(0, True), helper(0, False))