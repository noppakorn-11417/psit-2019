"""psit"""
def main(price, promo, free, minimum, qty=0):
    """despactip"""
    pack = minimum//(promo+free)
    qty = pack*(promo+free)
    if minimum%(promo+free) >= promo:
        qty, pack = qty+free+promo, pack+1
    else:
        qty += minimum%(promo+free)
    print((qty-(pack*free))*price, qty)
main(int(input()), int(input()), int(input()), int(input()))
