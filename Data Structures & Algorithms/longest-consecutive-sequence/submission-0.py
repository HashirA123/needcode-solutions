class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_size = 0

        for i in s:
            count = i
            while count+1 in s:
                count += 1
            max_size = max(max_size, count-i+1)
        
        return max_size