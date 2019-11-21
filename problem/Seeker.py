"""psit"""
def main(text, chk, ans):
    """prime nnumber"""
    for i in range(len(text)):
        if text[i] in "0123456789":
            chk.append(text[i])
        elif chk != []:
            ans.append(int("".join(chk)))
            chk.clear()
    print(sum(ans))
main(input()+" ", [], [])
