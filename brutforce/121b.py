arr = [7, 1, 5, 3, 6, 4]

buy_date = arr.index(min(arr))         
s_arr = arr[buy_date:]                
sell_price = max(s_arr)               

sell_index = arr.index(sell_price, buy_date)  

if sell_price > arr[buy_date]:
    print(f"Buy at {arr[buy_date]} (Day {buy_date+1}), sell at {sell_price} (Day {sell_index+1})")
else:
    print("No profit opportunity 😢")
