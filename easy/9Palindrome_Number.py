class Solution:
    def isPalindrome(self, x: int) -> bool:

        num_str = str(x)

        if(num_str[0] == "-"):
            return False
        
        num_body = num_str

        if len(num_body) == 1:
            swapped_str = num_body
        else:
            swapped_str = num_str[::-1]

        swapped_number = int(swapped_str)

        return swapped_number == x