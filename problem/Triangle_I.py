"""pair"""
def main(wood1, wood2, wood3):
    """triagle"""
    if wood2 >= wood1:
        wood1, wood2 = wood2, wood1
    if wood3 >= wood1:
        wood1, wood3 = wood3, wood1
    print("Yes" if abs(((wood1**2)+(wood2**2)+(wood3**2)-wood1**2)-(wood1**2)) <= 0.01 else "No")
main(float(input()), float(input()), float(input()))
