"""psit"""
def main(text, chk):
    """prime nnumber"""
    chk += [text[0]]
    for i in text[1:]:
        if i in chk:
            chk.append(i)
        else:
            print("%i%s"%(len(chk), chk[0]), end="")
            chk.clear()
            chk.append(i)
main(input()+ " ", [])
