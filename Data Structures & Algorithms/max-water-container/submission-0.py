class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # make greedy choice to move the smaller
        # value bar pointer

        l, r = 0, len(heights) - 1

        max_val = 0

        while l < r:
            s = (r-l) * min(heights[l], heights[r])
            max_val = max(max_val, s)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_val