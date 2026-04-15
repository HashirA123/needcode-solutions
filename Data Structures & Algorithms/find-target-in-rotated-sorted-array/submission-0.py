class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1


        while l < r:
            
            mid = (l+r) // 2

            if mid == l or mid == r:
                break

            # left side unsorted
            if nums[mid] < nums[l] and (target <= nums[mid] or target >= nums[l]):
                r = mid
            # right side unsorted
            elif nums[mid] > nums[r] and (target >= nums[mid] or target <= nums[r]):
                l = mid
            elif target <= nums[mid] and target >= nums[l]:
                r = mid
            else:
                l = mid
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1


            
