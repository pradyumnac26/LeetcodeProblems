class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        max_remap = None
        for ch in s:
            if ch != '9':
                max_remap = ch
                break
        max_val = int(s.replace(max_remap, '9')) if max_remap else int(s)

        min_remap = None
        for ch in s:
            if ch != '0':
                min_remap = ch
                break
        min_val = int(s.replace(min_remap, '0')) if min_remap else int(s)

        return max_val - min_val
