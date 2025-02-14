class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        m_profit = 0
        for i in range(1,len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                profit = prices[i] - buy_price
                m_profit = max(m_profit,profit)
        return m_profit

        