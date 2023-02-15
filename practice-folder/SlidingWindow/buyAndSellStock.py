# Problem:
# stock_price = [310,315,275,295,260,270,290,230,255,250]
# return the maximum profit that can be made
# by buying the selling one share of that stock.

def buyStock(array):
  min_price , max_profit = float ('inf'), 0
  for price in array:
    max_profit_sell_today = price - min_price
    max_profit = max(max_profit, max_profit_sell_today)
    min_price = min(min_price, price)
  return max_profit

print(buyStock([310,315,275,295,260,270,290,230,255,250]))

# first loop,
# max_profit_sell_today = 310 - float('inf') --> this means you minus infinity, which guarantees
# a negative value for the first iteration.
# max_profit = max(flot('inf'), 310)

def max_profit(prices):
    if not prices:
        return 0

    max_prof = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_prof = max(max_prof, prices[i] - min_price)
    return max_prof

print(max_profit([310,315,275,295,260,270,290,230,255,250]))


