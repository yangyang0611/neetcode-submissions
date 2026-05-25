class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            l = prices[left]
            r = prices[right]
            if r < l:
                left = right
            else:
                profit = r - l
                max_profit = max(profit, max_profit)
            right += 1
        return max_profit