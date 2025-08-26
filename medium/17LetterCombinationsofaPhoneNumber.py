class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result: list[str] = [""]
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            edit = phone_digits[digits]
            chars = list(edit)
            return chars
        else:
            for digit in digits:
                if digit in phone_digits:
                    letters = phone_digits[digits]
                    new_result: list[str] = []
                    for prefix in result:
                        for ch in letters:
                            new_result.append(prefix + ch)
                    result = new_result
            return result