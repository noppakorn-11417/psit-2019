"""stamp"""
def main(time, promo, stamp, stam_promo, discount):
    """stamp"""
    sum_price = 0
    stamp_qty = 0
    for _ in range(time):
        price = int(input())
        while stamp_qty >= stam_promo and price > 0:
            price -= discount
            stamp_qty -= stam_promo
        price = max(0, price)
        stamp_qty += (price//promo)*stamp
        sum_price += price
    print(sum_price, stamp_qty, sep="\n")
main(int(input()), int(input()), int(input()), int(input()), int(input()))
