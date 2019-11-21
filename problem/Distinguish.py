"""pair"""
def main(high):
    """try to use condition in print function"""
    print("You're hit the door edge." if high > 180 else "Nothing happens.")
main(float(input()))
