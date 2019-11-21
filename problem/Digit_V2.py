"""EZ"""
def digitv2(text):
    """EZ"""
    if "thousand" in text:
        return 4
    elif "hundred" in text:
        return 3
    elif [i for i in ["teen", "ty", "ten", "eleven", "twelve"] if i in text]:
        return 2
    else:
        return 1
print(digitv2(input()))
