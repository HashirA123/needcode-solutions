class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        store = {}
        counter = 0

        start = 0
        end = 0

        while end < len(s):
            rightVal = s[end]

            store[rightVal] = store.get(rightVal, 0) + 1
            while store[rightVal] > 1 and start < end:
                store[s[start]] -= 1
                start += 1
            
            counter = max(counter, end-start+1)
            end += 1
        
        return counter