"""psit"""
def main(num):
    """despacito"""
    for i in range(-(num//2), (num//2)+1):
        for j in range(-(num//2), (num//2)+1):
            print("%02d"%((num//2)+1-abs(abs(j)-abs(i))), end=" ")
        print()
main((int(input())*2)-1)
