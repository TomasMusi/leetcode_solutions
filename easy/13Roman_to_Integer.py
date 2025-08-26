class Solution:
    def romanToInt(self, s: str) -> int:
        privileges: dict[str,int] = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }    

        i = 0
        total = 0
        n = len(s)

        while i < n:
            if i + 1 < n and s[i:i+2] in privileges:
                total += privileges[s[i:i+2]]
                i +=2
            else: 
                total += privileges[s[i]]
                i += 1
        return total
        