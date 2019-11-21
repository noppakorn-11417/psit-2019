"""fc inw bas"""
def main(num):
    """fc inw bas"""
    return [i[-1] for i in num[1:len(num)-1].split(",")]
print(*main(input()), sep="\n")
