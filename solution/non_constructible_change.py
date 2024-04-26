def nonConstructibleChange(coins):
    # Write your code here.
    sorted_coins = sorted(coins)
    min_value = 0
    for coin in sorted_coins:
        if coin > min_value + 1:
            break
        else:
            min_value += coin
    return min_value + 1