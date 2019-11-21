"""psit"""
def main(myx, myy, distance1, tarx, tary):
    """i love psit"""
    distance2 = float(input())
    if ((myx-tarx)**2+(myy-tary)**2)**0.5 < distance1+distance2:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
