class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        store_s = {}
        store_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            store_s[s[i]] = store_s.get(s[i], 0) + 1
            store_t[t[i]] = store_t.get(t[i], 0) + 1

        for key, val in store_s.items():
            if key not in store_t or store_t[key] != val:
                return False
        
        return True
