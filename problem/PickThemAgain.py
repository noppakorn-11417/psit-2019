"""psit"""
def main(json, lis):
    """despacito"""
    for i in json.split(" "):
        if int(i)%3 == 0 or int(i)%5 == 0:
            lis.append(i)
    if len(lis) > 0:
        return print(*lis[::-1], sep="\n")
    return print("Nope")
main(input(), [])
