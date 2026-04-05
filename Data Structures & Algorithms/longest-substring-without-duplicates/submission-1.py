class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring = sliding window

        # hash map to know if a character has been seen before

        store = defaultdict(int)

        max_l = 0

        l = 0
        r = 0

        while r < len(s):
            right_val = s[r]
            store[right_val] += 1

            while store[right_val] > 1:
                store[s[l]] -= 1
                l += 1 
            max_l = max(max_l, r-l+1)

            r += 1
        
        return max_l