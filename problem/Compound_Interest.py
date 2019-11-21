"""EZ"""
def main(money, rate, year):
    """ez"""
    for _ in range(year):
        money = money*(1+rate/100)
    print("%.2f"%money)
main(int(input()), float(input()), int(input()))
