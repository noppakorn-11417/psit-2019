"""psit"""
def main(num):
    """find mu for p duk"""
    print(sum([i if i%3 == 0 or i%5 == 0 else 0 for i  in range(num+1)]))
main(int(input()))
