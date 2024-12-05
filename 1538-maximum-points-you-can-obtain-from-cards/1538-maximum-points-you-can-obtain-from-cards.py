class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0 
        rsum = 0
        rightInd = len(cardPoints)-1
        maxsum = 0 
        for i in range(k) : 
            lsum = lsum + cardPoints[i]
        maxsum = lsum
        for i in range(k-1, -1, -1) : 
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[rightInd]
            rightInd = rightInd -1
            maxsum = max(maxsum, lsum + rsum)
        return maxsum
        
        