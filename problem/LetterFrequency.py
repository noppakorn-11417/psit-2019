"""fc inw bas"""
def main(text):
    """fc inw bas"""
    maxdata = "", 0
    for i in set(text):
        if i in "qwertyuioplkjhgfdsazxcvbnm" and text.count(i) > maxdata[1]:
            maxdata = i, text.count(i)
    print(maxdata[0])
main(input().lower())
