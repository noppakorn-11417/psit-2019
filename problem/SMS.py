"""EZ"""
def nokia():
    """i sleep"""
    sms = []
    pin = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    for _ in range(int(input())):
        pin_input, times = int(input()), int(input())
        if pin_input != 1:
            sms += [pin[pin_input-2][(times%len(pin[pin_input-2]))-1]]
        else:
            sms = delete_this(times, sms)
    if not sms:
        return print("null")
    print("".join(sms))
def delete_this(amount, sms):
    """EZ"""
    for _ in range(amount):
        if sms:
            sms.pop(-1)
    return sms
nokia()
