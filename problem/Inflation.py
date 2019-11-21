"""psit"""
def cal(money, year):
    """i love marinepa"""
    for _ in range(year):
        money = (money*10381)//10000
    print("%d.%02d"%(money//100, money%100))
cal(int(float(input())*100), int(input()))
