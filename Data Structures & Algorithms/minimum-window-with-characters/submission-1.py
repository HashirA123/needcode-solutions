class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # while we have all t val, make smaller
        # is we dont have all, make bigger

        l, r, = 0, 0
        # need original to keep track of what char/freq is in t
        original = defaultdict(int)

        for i in t:
            original[i] += 1

        need = len(original) # the number of char/freq matches needed
        have = 0 # the number of char/freq matches we have

        store = defaultdict(int)

        min_size = float('inf')

        res = [-1, -1] # -1 incase we dont find any so we return ""

        while r < len(s):
            store[s[r]] += 1

            # check to see if we have a mathc
            if s[r] in original:
                if store[s[r]] == original[s[r]]:
                    have += 1

            while have == need:
                # if have == need, means we can check for min size
                # and keep making the window smaller to see how small
                # we can make while keeping have == need
                if r-l+1 < min_size:
                    min_size = r-l+1
                    res[0], res[1] = l, r
                if s[l] in original and store[s[l]] > 0:
                    store[s[l]] -= 1
                    if store[s[l]] < original[s[l]]:
                        have -= 1
                l += 1 # must make smaller at each iteration
            # this outside basically means keep making bigger no matter 
            # to make sure we can get have == need
            r += 1

        if res[0] == -1:
            return ""
        else:    
            return s[res[0]:res[1]+1]