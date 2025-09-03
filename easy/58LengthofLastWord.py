class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()

        words = s.split(" ")

        last_word = words[-1]

        return len(last_word)