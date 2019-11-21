"""psit week3"""
def sign(text):
    """make sign"""
    cal = sum([int(text[i]) for i in range(0, 13)])+int(text[10:13])*10
    cal += (1000)*(cal < 1000)
    print("%04d"%(cal%10000))
sign(input())
