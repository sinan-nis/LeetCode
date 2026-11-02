class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        counter = 0
        char = 0
        boolean = True

        if strs[0] == "":
            return prefix

        if len(strs) ==1:
            return strs[0]

        while boolean:
            if char >= len(strs[0]):
                return prefix
            first = strs[0][char]
            
            for s in strs:
                if char >= len(s):
                    return prefix
                if first == s[char]:
                    counter+=1
                    if counter < len(strs):
                        continue
                    elif counter == len(strs):
                        prefix += s[char]
                        counter = 0
                elif first != s[char]:
                    boolean = False
                    return prefix
            char += 1      
                    
                    

                

            