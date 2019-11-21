"""psit"""
def main(limit, count=0, weight=0):
    """ez"""
    chik = sorted(list(map(int, input().split())))
    for i in chik:
        if weight+i <= limit:
            weight += i
            count += 1
    print(count)
main(int(input()))
