"""psit"""
import string as s
def main(text):
    """prime nnumber"""
    for i in text:
        if not i in s.ascii_letters+" ":
            text = text.replace(i, "")
    for i in text.split(" "):
        if len(i) > 6:
            print(i, end=" ")
main(input())
