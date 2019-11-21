"""midterm"""
def main(num, cal=0):
    """ chk hasrad number"""
    for i in num:
        if int(i) == 0:
            print("No")
            continue
        if int(i) < 0:
            i = str(abs(int(i)))
        for j in i:
            cal += int(j)
        if int(i)%cal == 0 and (int(i) != 0):
            print("Yes")
        else:
            print("No")
        cal = 0
main([input() for i in range(10)])
