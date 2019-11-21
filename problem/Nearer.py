"""despacito"""
def main(alice, bob, cart):
    """despacito"""
    cal1 = abs(alice-cart)
    cal2 = abs(bob-cart)
    if cal1 < cal2:
        print("Alice", min(cal1, cal2))
    elif cal1 > cal2:
        print("Bob", min(cal1, cal2))
    else:
        print("Sundaes", min(cal1, cal2))
main(int(input()), int(input()), int(input()))
