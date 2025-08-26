

from typing import List

str_list = ["Flowers", "Flying", "flee"]

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    # Checks for the shortest word in the list (because there cannot be longer prefix than shortest word)    
    shortest = min(strs, key=len)
    
    # goes for characters and index
    # i = 0, ch = 'f'
    # i = 1, ch = 'l'
    # i = 2, ch = 'o'
    # etc.
    for i, ch in enumerate(shortest):
        # loops the whole array.
        for word in strs:
            # first loop: all of them have F
            # second loop: all of them have l
            # third loop: error one of them has 0
            if word[i].lower() != ch.lower(): 
                return shortest[:i]
    return shortest

print(longestCommonPrefix(str_list))
