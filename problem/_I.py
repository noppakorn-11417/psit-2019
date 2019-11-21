"""psit"""
def main(myx, myy, distance, tarx, tary):
    """i love psit"""
    if abs(myx-tarx) < distance and abs(myy-tary) < distance:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
