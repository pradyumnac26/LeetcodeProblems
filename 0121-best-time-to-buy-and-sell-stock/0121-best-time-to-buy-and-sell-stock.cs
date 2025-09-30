public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0; 
        int r = 1 ; 
        int maxprofit = 0;
        while (r < prices.Length ) { 
            if (prices[r] > prices[l]) { 
                int profit = prices[r] - prices[l];
                maxprofit = Math.Max(maxprofit, profit);
            }
            else { 
                l =r ;
            }
            r = r +1 ;
        }
        return maxprofit;
        
        
    }
}