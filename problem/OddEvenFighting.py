"""psit"""
def main(num, odd=0, even=0):
    """find mu for p duk"""
    while num != 0:
        even, odd, num = even+num*(num%2 == 0), odd+num*(num%2), int(input())
    print("Draw"*(even == odd)+("Odd"*(even < odd))+"Even"*(even > odd), (odd+even-min(odd, even)))
main(int(input()))
