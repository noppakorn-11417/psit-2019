"""EZ"""
def main(game_price, coupon1, coupon2):
    """EZ"""
    if game_price < float(coupon1[1]) and game_price < float(coupon2[1]):
        return print("Nope")
    cal_coupon1 = game_price-(float(coupon1[0])*(game_price >= float(coupon1[1])))
    cal_coupon2 = game_price*(1-((float(coupon2[0])/100)*(game_price >= float(coupon2[1]))))
    if cal_coupon1 > cal_coupon2:
        print("2 %.1f"%cal_coupon2)
    elif cal_coupon1 < cal_coupon2:
        print("1 %.1f"%cal_coupon1)
    else:
        if float(coupon1[1]) < float(coupon2[1]):
            print("1 %.1f"%cal_coupon1)
        elif float(coupon2[1]) < float(coupon1[1]):
            print("2 %.1f"%cal_coupon2)
        else:
            print("1 %.1f"%cal_coupon1)
main(float(input()), input().split(), input().split())
