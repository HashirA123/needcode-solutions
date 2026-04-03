class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char) - ord('a')] += 1
            
            key = tuple(arr)
            if key not in store:
                store[key] = []
            store[key].append(word)

        res = []

        for key in store:
            res.append(store[key])

        return res