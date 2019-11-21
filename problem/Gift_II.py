"""pair"""
def makelist(count, lista):
    """manual for loop to find gilf"""
    if count <= 8:
        return makelist(count+1, lista+[(int(input()))])
    print(*list(filter(lambda x: x%2 == 0, lista)))
makelist(1, [])
