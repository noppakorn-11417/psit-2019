"""EZ"""
def main():
    """EZ"""
    milk_price, promo1, free_qty1, promo2 = float(input()), float(input()), \
    float(input()), float(input())
    free_qty2, money = float(input()), float(input())
    milk_qty = money//(milk_price)
    milk_cap = milk_qty
    milk_bot = milk_qty
    while (milk_cap >= promo1 or milk_bot >= promo2) and (promo1+promo2) != 0:
        cap, bot = 0, 0
        if milk_cap >= promo1 and promo1 != 0:
            milk_cap -= promo1
            cap = 1
        if milk_bot >= promo2 and promo2 != 0:
            milk_bot -= promo2
            bot = 1
        milk_qty += (bot*free_qty2)+(cap*free_qty1)
        milk_cap += (bot*free_qty2)+(cap*free_qty1)
        milk_bot += (bot*free_qty2)+(cap*free_qty1)
    print(int(milk_qty))
main()
