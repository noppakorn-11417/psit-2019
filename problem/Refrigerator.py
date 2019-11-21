"""psit"""
def main(day, count=0):
    """ez"""
    day = sorted(list(map(int, input().split())))
    while 0 != day[0]:
        day = sorted([day[0]]+list(map(lambda x: -1+x, day[1:])))
        count += 1
    print(count)
main(int(input()))
