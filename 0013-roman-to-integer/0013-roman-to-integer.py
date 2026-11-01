class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for index, char in enumerate(s):
            if char == "I":
                if index+1 < len(s) and s[index+1] == "V":
                    result += 4
                elif index+1 < len(s) and s[index+1] == "X":
                    result += 9
                else:
                    result +=1
            elif char == "V":
                if index-1 >= 0:
                    if s[index-1] == "I":
                        continue
                result += 5
            elif char == "X":
                if index-1 >= 0:
                    if s[index-1] == "I":
                            continue
                if index+1 < len(s) and s[index+1] == "L":
                    result += 40
                elif index+1 < len(s) and s[index+1] == "C":
                    result += 90
                else:
                    result += 10
            elif char == "L":
                if index-1 >= 0:
                    if s[index-1] == "X":
                            continue
                result += 50
            elif char == "C":
                if index-1 >= 0:
                    if s[index-1] == "X":
                            continue
                if index+1 < len(s) and s[index+1] == "D":
                    result += 400
                elif index+1 < len(s) and s[index+1] == "M":
                    result += 900
                else:
                    result += 100
            elif char == "D":
                if index-1 >= 0:
                    if s[index-1] == "C":
                        continue
                result += 500
            elif char == "M":
                if index-1 >= 0:
                    if s[index-1] == "C":
                        continue
                result += 1000
        return result