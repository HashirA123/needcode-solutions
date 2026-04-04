class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if ord(s[l].lower()) < ord('a') or ord(s[l].lower()) > ord('z'):
                if ord(s[l].lower()) < ord('0') or ord(s[l].lower()) > ord('9'):
                    l += 1
                    continue
            if ord(s[r].lower()) < ord('a') or ord(s[r].lower()) > ord('z'):
                if ord(s[r].lower()) < ord('0') or ord(s[r].lower()) > ord('9'):
                    r -= 1
                    continue
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True