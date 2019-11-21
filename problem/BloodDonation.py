"""EZ"""
def appove(age, weight, donate, ans="Yes"):
    """EZ"""
    if age > 70 or weight < 45 or age <= 16:
        ans = "No"
    if donate < 1 and age > 55:
        ans = "No"
    if age == 17 or (60 <= age <= 70):
        if input() != "True":
            ans = "No"
    print(ans)
appove(int(input()), int(input()), int(input()))
