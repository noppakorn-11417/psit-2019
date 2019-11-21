"""EZ"""
def diff(text):
    """555"""
    for i in range(len(text)-1, -1, -1):
        print((i)*" "+text[:len(text)-i])
    for i in range(len(text)-1, 0, -1):
        print(text[len(text)-i:])
diff(input())
