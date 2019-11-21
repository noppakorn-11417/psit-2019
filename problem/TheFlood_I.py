"""psit"""
def main(sand_bag, count=0):
    """ez"""
    time = sorted(list(map(int, sand_bag.split())))
    while 0 not in time:
        time = sorted([time[0]]+[-1+i for i in time[1:]])
        count += 1
    print(count)
main(input())
