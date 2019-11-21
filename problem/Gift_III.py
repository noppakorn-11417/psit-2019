"""day"""
def main(count, num1, ans1, ans2, distance):
    """love psit"""
    if count > 1:
        value = int(input())
        distance += abs(value-ans1)
        if value == ans1:
            ans1 = ans1
        elif value > ans1:
            ans1, ans2 = value, ans1
        elif value >= ans2:
            ans2 = value
    if ans2 >= ans1:
        ans1, ans2 = ans2, ans1
    if ans2 >= ans1:
        ans1, ans2 = ans2, ans1
    if count < num1:
        return main(count+1, num1, ans1, ans2, distance)
    if distance == 0:
        print("Exit")
    else:
        print(ans2)
main(1, int(input()), int(input()), 0, 0)
