class Solution(object):
    def addBinary(self, a: str, b:str) -> str:
        # zarovnání délky (kratší doplníme nulami vlevo)
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        # -1 -1 -1 znamená, že jdeme od prava do leva. (od konce po začátek.)
        for i in range(max_len - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

            total = bit_a + bit_b + carry

            result.append(str(total % 2))

            carry = total // 2

        if carry:
            result.append("1")

        result.reverse() 
        return "".join(result)



s = Solution()
print(s.addBinary("11", "1"))