"""despacito"""
def mian(digi):
    """despacito"""
    while digi != "0":
        while len(digi) > 1:
            ans = 0
            for i in digi:
                ans += int(i)
            digi = str(ans)
        print(digi)
        digi = input()
mian(input())
