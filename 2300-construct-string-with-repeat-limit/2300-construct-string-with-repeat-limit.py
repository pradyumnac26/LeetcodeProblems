from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Build a max-heap (using negative ord values for lexicographical order)
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(max_heap)  # Convert the list into a heap
        result = []

        # Step 2: Process the heap to construct the string
        while max_heap:
            # Pop the largest available character
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)  # Use up to repeatLimit times
            result.append(char * use)  # Append the character to the result

            remaining = count - use  # Remaining count of the current character

            # Step 3: If we exceed repeatLimit and the heap is not empty, break the sequence
            if remaining > 0 and max_heap:
                next_char_neg, next_count = heappop(max_heap)  # Next largest character
                next_char = chr(-next_char_neg)
                result.append(next_char)  # Append the next largest character once
                
                # Push the characters back into the heap with updated counts
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, remaining))  # Reinsert the current character

        return "".join(result)
