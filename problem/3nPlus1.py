"""nani sore"""
def cal(num, count=1):
    """cal"""
    while num > 1:
        if num%2 == 0:
            num /= 2
        else:
            num = (num*3)+1
        count += 1
    return count
def print_count(num):
    """print loop"""
    while num != 0:
        print(cal(num))
        num = int(input())
print_count(int(input()))
