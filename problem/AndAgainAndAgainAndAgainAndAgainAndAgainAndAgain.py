"""psit week3"""
def sign(text, ans, temp=0):
    """make sign"""
    for i in text:
        if not i.lower() in "qwertyuioplkjhgfdaszxcvbnm ":
            text = text.replace(i, "")
    text_list = sorted(text.split())
    for i in text_list:
        for j in "aeiou":
            temp += i.lower().count(j)
            if temp >= 2:
                ans.append(i)
                break
        temp = 0
    if ans != []:
        return print(*ans, sep="\n")
    print("Nope")
sign(input(), [])
