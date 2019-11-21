"""psit"""
def main(json, lis):
    """despacito"""
    for i in json[1:][::-1][1:][::-1].replace(" ", "").split(","):
        if int(i)%2 == 0:
            lis.append(i)
    if len(lis) > 0:
        return print(*lis, sep="\n")
    return print("Nope")
main(input(), [])
