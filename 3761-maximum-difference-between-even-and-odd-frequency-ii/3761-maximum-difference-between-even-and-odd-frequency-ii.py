class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        res = float('-inf')
        
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                # Create prefix sums for counts of a and b
                count_a = [0] * (n + 1)
                count_b = [0] * (n + 1)
                
                for i in range(1, n + 1):
                    count_a[i] = count_a[i - 1] + (int(s[i - 1]) == a)
                    count_b[i] = count_b[i - 1] + (int(s[i - 1]) == b)
                
                # Stores max (count_b[j] - count_a[j]) for each parity
                g = [[float('-inf')] * 2 for _ in range(2)]
                j = 0
                
                for i in range(k, n + 1):
                    while i - j >= k and count_a[i] > count_a[j] and count_b[i] > count_b[j]:
                        parity_a = count_a[j] % 2
                        parity_b = count_b[j] % 2
                        g[parity_a][parity_b] = max(g[parity_a][parity_b], count_b[j] - count_a[j])
                        j += 1
                    
                    parity_a = count_a[i] % 2
                    parity_b = count_b[i] % 2
                    best = g[1 - parity_a][parity_b]
                    
                    if best != float('-inf'):
                        res = max(res, (count_a[i] - count_b[i]) + best)
        
        return res if res != float('-inf') else -1