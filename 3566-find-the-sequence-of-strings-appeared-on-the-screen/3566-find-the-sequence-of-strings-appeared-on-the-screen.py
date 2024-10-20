from typing import List

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        sequence = []
        screen = ""
        
        # Start building the sequence to match the target
        for i in range(len(target)):
            if i == 0:
                # Start with 'a'
                screen = 'a'
                sequence.append(screen)
            
            # Keep appending 'a' until the length matches the target length
            while len(screen) <= i:
                screen += 'a'
                sequence.append(screen)
            
            # Increment last character to match the target character
            while screen[i] != target[i]:
                last_char = screen[i]
                next_char = chr(((ord(last_char) - ord('a') + 1) % 26) + ord('a'))
                screen = screen[:i] + next_char
                sequence.append(screen)
        
        return sequence
