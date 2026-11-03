class Solution:
    def isValid(self, s: str) -> bool:
        
        liste = []
        characters = {
            ")": "(",
            "}": "{",
            "]": "["
        } 

        for char in s:
            if char not in characters:
                liste.append(char)
            else:
                if len(liste) == 0:
                    return False

                if liste[-1] == characters[char]:
                    liste.pop()
                else:
                    return False
        if len(liste) >= 1:
                    return False
        return True

            
             
