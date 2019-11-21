"""psit"""
def main(num, count=0):
    """prime nnumber"""
    for i in range(2, num+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            count += 1
    print(count)
main(int(input()))
