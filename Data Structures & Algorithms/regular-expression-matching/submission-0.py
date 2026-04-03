class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        def helper(i, j, store):
            if (i,j) in store:
                return store[(i, j)]

            if i == len(s) and j == len(p):
                return True
            elif j == len(p):
                return False
            
            matched = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                # keep trying to use the star
                store[(i, j)] = (matched and helper(i+1, j, store) or # can only use if match condition is true
                    helper(i, j+2, store)) # skip the star
                return store[(i, j)]
            # if no star
            if matched:
                store[(i, j)] = helper(i+1, j+1, store)
                return store[(i, j)]

            # if didnt match, return false
            store[(i, j)] = False
            return store[(i, j)]
        store = {}
        return helper(0, 0, store)
                 
            




