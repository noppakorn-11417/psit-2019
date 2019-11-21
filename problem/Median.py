"""fc inw bas"""
def main(num):
    """fc inw bas"""
    if num%2 != 0:
        return print("%.1f"%sorted([int(input()) for i in range(num)])[num//2])
    cal = sorted([int(input()) for i in range(num)])
    print("%.1f"%(sum([j for i, j in enumerate(cal) if i == num//2 or i == num//2-1])/2))
main(int(input()))
