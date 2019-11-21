"""fc inw bas"""
def main(num, text):
    """fc inw bas"""
    if num > 26:
        num %= 26
    if num < -26:
        num = (abs(num)%26)*-1
    ceasar = 0
    ans = []
    ascii_low = "zxcvbnmlkjhgfdsaqwertyuiop"
    for i in text:
        if i in ascii_low:
            ceasar = ord(i)+num
            if ceasar < 97:
                ceasar += 26
            if ceasar > 122:
                ceasar -= 26
            ans.append(ceasar)
        elif i in ascii_low.upper():
            ceasar = ord(i)+num
            if ceasar < 65:
                ceasar += 26
            if ceasar > 90:
                ceasar -= 26
            ans.append(ceasar)
        else:
            ans.append(ord(i))
    print("".join([chr(i) for i in ans]))
main(int(input()), input())
