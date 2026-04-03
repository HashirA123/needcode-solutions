class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # make the key the unique encoding list
        for s in strs:
            key = [0] * 26

            for char in s:
                # use ord() to get char position
                key[ord(char) - ord('a')] += 1
            # list not hashable, tuple is
            res[tuple(key)].append(s)
        
        final = []
        for key, val in res.items():
            final.append(val)
        
        return final

                
                
