class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        store = {}

        def helper(i, j, store):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in store:
                return store[(i,j)]
            
            if text1[i] == text2[j]:
                store[(i, j)] = 1 + helper(i+1, j+1, store)
            else:
                # try to increase either and take the larger/longer one
                store[(i, j)] = max(helper(i+1, j, store), helper(i, j+1, store))
            
            return store[(i, j)]
        
        return helper(0, 0, store)