class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        numb = []

        for l in digits:
            numb.append(l)

        i = len(numb) - 1                 
        digit = numb[i]
        digit += 1
        while len(str(digit)) > len(str(numb[i])):   
            numb[i] = 0                   
            i -= 1                        
            if i < 0:                     
                numb.insert(0, 1)
                return numb
            digit = numb[i] + 1           
        numb[i] = digit
        return numb