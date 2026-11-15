class Solution:

    def encode(self, strs: List[str]) -> str:
        dicto = []
        for i in strs:
            s=len(i)
            dicto.append(f"{s}#{i}")
        s=''.join(dicto)
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res