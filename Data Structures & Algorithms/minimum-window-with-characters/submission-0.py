class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # while we have all t val, make smaller
        # is we dont have all, make bigger

        l, r, = 0, 0

        original = defaultdict(int)

        for i in t:
            original[i] += 1

        need = len(original)
        have = 0

        store = defaultdict(int)

        min_size = float('inf')

        res = [-1, -1]

        while r < len(s):
            store[s[r]] += 1

            if s[r] in original:
                if store[s[r]] == original[s[r]]:
                    have += 1

            while have == need:
                if r-l+1 < min_size:
                    min_size = r-l+1
                    res[0], res[1] = l, r
                if s[l] in original and store[s[l]] > 0:
                    store[s[l]] -= 1
                    if store[s[l]] < original[s[l]]:
                        have -= 1
                l += 1
            r += 1

        if res[0] == -1:
            return ""
        else:    
            return s[res[0]:res[1]+1]