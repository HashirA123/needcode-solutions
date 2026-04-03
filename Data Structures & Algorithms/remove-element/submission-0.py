class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front = 0

        finder = 0

        while finder < len(nums):
            if nums[finder] != val:
                nums[front] = nums[finder]
                front += 1
                finder += 1
            else:
                finder += 1
        
        return front