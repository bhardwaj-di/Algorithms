def maxProfit(self, prices: List[int]) -> int:
    temp = prices[0]
    profit_dict = {temp : 0}
    for i in range(len(prices)):
        if prices[i] < temp:
            profit_dict[prices[i]] = profit_dict.pop(temp)
            temp = prices[i]
        else:
            if (profit_dict[temp] < (prices[i] - temp)):
                profit_dict[temp] = (prices[i] - temp)
    return profit_dict[temp]