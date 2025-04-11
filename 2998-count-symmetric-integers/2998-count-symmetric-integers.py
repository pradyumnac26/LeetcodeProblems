class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue  # skip odd length numbers
            
            n = len(s) // 2
            first_half = s[:n]
            second_half = s[n:]
            
            sum1 = sum(int(digit) for digit in first_half)
            sum2 = sum(int(digit) for digit in second_half)
            
            if sum1 == sum2:
                count += 1
                
        return count
