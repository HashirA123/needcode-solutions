class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        index = 0

        if len(strs) == 1:
            return strs[0]

        while True:
            for i in range(len(strs)):
                if i < len(strs) - 1:
                    if index < len(strs[i]) and index < len(strs[i+1]):
                        if strs[i][index] != strs[i+1][index]:
                            return ans
                    else:
                        return ans
            
            ans += strs[0][index]
            index += 1