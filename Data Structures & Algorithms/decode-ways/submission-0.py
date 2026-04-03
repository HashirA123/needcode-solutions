class Solution:
    def numDecodings(self, s: str) -> int:
        letter_num = {}

        counter = 1
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letter_num[i] = counter
            counter += 1
        
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i == len(s): # we got to the end, meaning one valid path
                return 1
            if s[i] == "0":
                return 0

            # two choices, take this val, or the next
            res = helper(i+1) # jump by one, meaning we took the current
                        # number as a letter
            # seconds case, take two numbers, if they work
            if (i+1 < len(s) and (int(s[i]) < 2 or (int(s[i]) < 3 and int(s[i+1]) < 7))):
                res += helper(i+2) # jump two since these two numbers work
            
            memo[i] = res
            return memo[i]

        return helper(0)