"""EZ"""
def main(small, big, want):
    """ez"""
    wall_want_small = want-min((want//5)*5, big*5)
    if wall_want_small <= small:
        return print(wall_want_small)
    print("-1")
main(int(input()), int(input()), int(input()))
