"""despacito"""
def main(milk_price, promo, free_qty, money):
    """despacito"""
    milk_qty = money//(milk_price)
    get_milk = milk_qty
    while get_milk >= promo and  promo != 0:
        milk_qty += free_qty
        get_milk -= promo-free_qty
    print(milk_qty)
main(int(input()), int(input()), int(input()), int(input()))
