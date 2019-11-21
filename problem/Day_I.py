"""psit"""
def main(day):
    """love psit"""
    if day%400 == 0 or (day%4 == 0 and day%100 != 0):
        print("Yes")
    else:
        print("No")
main(int(input()))
