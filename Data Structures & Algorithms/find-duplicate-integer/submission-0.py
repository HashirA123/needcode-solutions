class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # think of the elements in the list as
        # pointers to the next index
        #  0, 1, 2
        # [1, 2, 2]
        # at 0 we point to 1, then 1 points to 2,
        # and 2 points to itself.
        # then use the fast/slow pointer to find loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # the first loop finds the "loop", second
        # finds the begining of the loop
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
