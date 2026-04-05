class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window again, but need to keep track of
        # most popular element, so we know which others
        # to count as replaced

        max_size = 0
        max_val = 0

        l, r = 0, 0

        store = defaultdict(int)

        while r < len(s):
            store[s[r]] += 1

            max_val = max(max_val, store[s[r]]) # this basically just tracks the 
            # best case, meaning even if our element of max value no longer is
            # in the window, we dont bother updating until we find a value
            # thats bigger. This tracks since we only care when are window
            # size is allowed to be bigger than it is now.
                                
            while ((r-l+1) - max_val) > k:
                store[s[l]] -= 1
                l += 1

            max_size = max(max_size, r-l+1)
            r += 1
        
        return max_size
