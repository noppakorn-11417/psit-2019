"""EZ"""
def kabata():
    """EZ"""
    for _ in range(int(input())):
        kabata_check(input())
def kabata_check(text):
    """ez"""
    text = text.replace("baka", "xxxx")
    grammar = ["bakka", "ba", "ta", "ka"]
    for i in grammar:
        text = text.replace(i, "")
    if not text:
        return print("yes")
    print("no")
 
kabata()
