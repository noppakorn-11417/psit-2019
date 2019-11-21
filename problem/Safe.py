"""psit"""
def safe(code, encode, ans=0):
    """ez"""
    for i, j in zip(code, encode):
        i, j = max(i, j), min(i, j)
        ans += min(abs(26-(ord(i)-ord(j))), abs((ord(i)-ord(j))))
    print(ans)
safe(input(), input())
