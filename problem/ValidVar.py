"""EZ"""
import string
def main():
    """test"""
    print(*[syntax_check(input().lstrip().rstrip()) for _ in range(int(input()))], sep="\n")
 
def syntax_check(text):
    """EZ"""
    if text in ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'None'\
, 'break', 'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def']:
        return "Invalid"
    if [i for i in text if i in string.punctuation and i != "_"]:
        return "Invalid"
    if text.count(" "):
        return "Invalid"
    if text[0].isdigit():
        return "Invalid"
    return "Valid"
main()
