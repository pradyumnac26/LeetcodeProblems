class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        residue = 0

        for i, ch in enumerate(s):
            seen.add(ch)                 # harmless if already present
            if len(seen) == (i + 1) % 3: # check EVERY prefix
                residue += 1

        return residue


        