"""ez"""
def inverter(text):
    """EZ"""
    print(text.replace("0", "x").replace("1", "y").replace("y", "0").replace("x", "1").lstrip("0"))
inverter(input())
