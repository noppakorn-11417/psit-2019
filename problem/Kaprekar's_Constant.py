"""despacito"""
def main(num):
    """despacito"""
    if int(num[1]) >= int(num[0]):
        num = num[1]+num[0]+num[2]+num[3]
    if int(num[2]) >= int(num[1]):
        num = num[0]+num[2]+num[1]+num[3]
    if int(num[3]) >= int(num[2]):
        num = num[0]+num[1]+num[3]+num[2]
    if int(num[2]) >= int(num[1]):
        num = num[0]+num[2]+num[1]+num[3]
    if int(num[1]) >= int(num[0]):
        num = num[1]+num[0]+num[2]+num[3]
    if int(num[2]) >= int(num[1]):
        num = num[0]+num[2]+num[1]+num[3]
    if int(num[::-1]) > int(num):
        num = num[::-1]
    return num
def cal(num, count=0, cal_num=0):
    """import chotipas"""
    while cal_num != "6174":
        cal_num = main(num)
        cal_num = str(int(cal_num)-int(cal_num[::-1]))
        num = "%04d"%int(cal_num)
        count += 1
    print(count)
cal(input())
