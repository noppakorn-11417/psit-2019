"""EZ"""
def main(old_text, new_text):
    """EZ"""
    text1 = text2 = ""
    print("".join(old_text))
    while old_text or new_text:
        text2 = ""
        if old_text:
            old_text.pop(0)
            text2 = "".join(old_text)
        if new_text:
            text1 += str(new_text.pop(0))
        print(text1+text2)
main(list(input()), list(input()))
