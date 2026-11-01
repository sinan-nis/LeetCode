class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        zahl = 0

        while n > 0:
            ziffer = n%10
            zahl = zahl * 10 + ziffer
            n = n//10
        
        if x == zahl:
            return True
        
        return False

