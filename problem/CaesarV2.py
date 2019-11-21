"""nani sore"""
def test(text):
    """nani sore"""
    text_list = [main(i, text) for i in range(26)]
    chk = []
    sum_aeiou = 0
    for i, j in enumerate(text_list):
        sum_aeiou += j.count("a")
        sum_aeiou += j.count("e")
        sum_aeiou += j.count("i")
        sum_aeiou += j.count("o")
        sum_aeiou += j.count("u")
        chk += [[sum_aeiou, i]]
        sum_aeiou = 0
    max_key = sorted(chk, key=lambda x: x[0], reverse=True)[0][1]
    print(main(max_key, text))
def main(num, text):
    """nanai sore"""
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
    return "".join([chr(i) for i in ans])
test(input())
