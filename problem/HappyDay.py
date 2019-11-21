"""fc inw bas"""
def main(qty):
    """fc inw bas"""
    count = 0
    for i in range(len(qty)):
        if int(qty[i]) >= 80 or (int(qty[i])-int(qty[i-1]) >= 10 and i != 0 and int(qty[i]) >= 20):
            count += 1
    print(count)
main(input().split(","))
