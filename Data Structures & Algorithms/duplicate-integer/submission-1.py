class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set(nums)

        if len(nums) > len(store):
            return True
        return False

