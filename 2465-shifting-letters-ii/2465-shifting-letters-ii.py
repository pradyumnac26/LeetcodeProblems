class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)
        
        # Build the difference array
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                diff[start] += 1
                diff[end + 1] -= 1
            else:  # Backward shift
                diff[start] -= 1
                diff[end + 1] += 1
        
        # Compute the net shifts using prefix sum
        net_shifts = [0] * n
        running_shift = 0
        for i in range(n):
            running_shift += diff[i]
            net_shifts[i] = running_shift
        
        # Apply shifts to the string
        result = []
        for i in range(n):
            shift = net_shifts[i] % 26  # Wrap around alphabet
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
