"""main"""
def forex(start_money, trade_count):
    """EZ"""
    buy_sell_rate = [['USD', (31.8, 32.7)], ['EUR', (40.1, 40.8)], \
    ['GBP', (51, 51.55)], ['AUD', (26.75, 27.2)], ['JPY', (0.275, 0.281)], \
    ['CNY', (4, 5.28)], ['TWD', (1.07, 1.095)], ['SGD', (24.65, 25.05)], \
    ['KRW', (0.026, 0.03)], ['HKD', (4.19, 4.25)], ['MYR', (8.9, 9.45)], ['SEK', (4.05, 4.35)], \
    ['CHF', (33.4, 34)], ['NZD', (25.2, 25.8)], ['CAD', (28, 28.9)], ['NOK', (4.15, 4.47)], \
    ['DKK', (5.15, 5.47)], ['PHP', (0.3, 0.75)], ['VAM', (0.00148, 0.00157)], \
    ['IDR', (0.00255, 0.00285)], ['INR', (0.3, 0.55)]]
 
    wallet = {'THB': start_money, 'USD': 0, 'EUR': 0, 'GBP': 0, 'AUD': 0, 'JPY': 0, 'CNY': 0,\
     'TWD': 0, 'SGD': 0, 'KRW': 0, 'HKD': 0, 'MYR': 0, 'SEK': 0, 'CHF': 0, 'NZD': 0, 'CAD': 0, \
     'NOK': 0, 'DKK': 0, 'PHP': 0, 'VAM': 0, 'IDR': 0, 'INR': 0}
 
    for _ in range(trade_count):
        data = input().split()
        buysell, types, money = data[0], data[1], data[2]
        if buysell == "BUY":
            buy(wallet, types, [i for i in buy_sell_rate if i[0] == types][0][1], int(money))
        else:
            sell(wallet, types, [i for i in buy_sell_rate if i[0] == types][0][1], int(money))

    for i in sorted([[i, wallet[i]] for i in wallet if wallet[i] >= 1], key=lambda x: tuple(x[0])):
        print("%s %.2f"%(i[0], i[1]))
 
def buy(wallet, types, rate, want):
    """EZ"""
    cal = min(wallet["THB"]//rate[1], want)
    wallet[types] += cal
    wallet["THB"] -= rate[1]*cal
 
def sell(wallet, types, rate, want):
    """EZ"""
    cal = min(wallet[types], want)
    wallet[types] -= cal
    wallet["THB"] += rate[0]*cal
 
 
forex(float(input()), int(input()))
