"""psit"""
def main(num, li1, list2):
    """find mu for p duk"""
    li1 = [[float(input()), float(input())] for i in range(num)]
    list2 = [li1[i][1]/li1[i][0] for i in range(num)]
    li1.sort(key=lambda x: x[0])
    for i in range(num):
        if li1[i][1]/li1[i][0] == max(list2):
            return print("%.2f %.2f"%(li1[i][0], li1[i][1]))
main(int(input()), [], [])
