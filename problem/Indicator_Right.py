"""psit"""
def main(width, high):
    """find mu for p duk"""
    for i in range((-high//2)+1, (high//2)+1):
        print((((high//2)-abs(i)))*" "+"*"*width)
main(int(input()), int(input()))
