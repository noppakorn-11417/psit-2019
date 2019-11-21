"""psit"""
def main(money, ans=0, coin_de=0):
    """ez"""
    coin = [25, 10, 5, 1]
    for i in range(4):
        coin_de = money//coin[i]
        money = max(0, money-(coin_de*coin[i]))
        ans += coin_de
    print(ans)
main(int(input()))
