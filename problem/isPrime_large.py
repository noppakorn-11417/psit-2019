"""psit"""
def main(num):
    """prime nnumber"""
    if num == 2:
        return print("YES")
    elif num > 1 and num%2 != 0:
        for i in range(3, int(num**0.5)+1, 2):
            if num%i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main(int(input()))
