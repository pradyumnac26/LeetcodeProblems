from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        HIGH = 10**7  

        for i in range(n + 1, HIGH + 1):
            s = str(i)
            if '0' in s:        
                continue
            h = Counter(map(int, s))

            is_beautiful = True
            for k, v in h.items():
                if k != v:
                    is_beautiful = False
                    break

            if is_beautiful:
                return i
