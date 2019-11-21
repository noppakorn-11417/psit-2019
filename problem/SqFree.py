"""psit"""
def main(number, ans=0):
    """fc inw nut"""
    for i in range(1, number+1):
        for j in range(2, int(i**0.5)+1):
            if i%j**2 == 0:
                ans -= 1
                break
    print(ans+number)
main(int(input()))
