class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = [h for _, h in envelopes]

        lis = []

        for h in heights:

            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(lis):
                lis.append(h)
            else:
                lis[left] = h

        return len(lis)




        