"""psit"""
def main(text, chk):
    """prime nnumber"""
    for i in range(len(text)):
        if 48 <= ord(text[i]) <= 57:
            chk.append(text[i])
        else:
            print(int("".join(chk))*text[i], end="")
            chk.clear()
main(input(), [])
