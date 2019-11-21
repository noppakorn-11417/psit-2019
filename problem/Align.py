"""psit week3"""
def sign():
    """make sign"""
    space = int(input())
    pos = input()
    txt = input()
    if pos == "left":
        print(txt.ljust(space))
    elif pos == "right":
        print(txt.rjust(space))
    elif pos == "center":
        if len(txt) % 2 == 1:
            txt = txt[::-1].center(space)
            print(txt[::-1])
        else:
            print(txt.center(space))
sign()
