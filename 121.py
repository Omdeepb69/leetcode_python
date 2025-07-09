prices = [7, 1, 5, 3, 6, 4]

def findMaxProfit(prices):
    max_profit = 0
    l,r=0,1
    
    while r < len(prices):
        if prices[r] > prices[l]:
            max_profit = max(max_profit,prices[r]-prices[l])
        else: 
            l=r
        r += 1
            
    return max_profit

if __name__ == "__main__":
    print(findMaxProfit(prices))
            