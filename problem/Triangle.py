"""despacito"""
def cal(num, count=2):
    """despacito"""
    for i in range(-num, 0):
        if i == -num:
            print("  "*(abs(i)-1)+"%02d"%abs(i))
        elif i == -num+1:
            print("  "*(abs(i)-1)+"%02d"%abs(i)+"  "+"%02d"%abs(i))
        else:
            count += 4
            print("  "*(abs(i)-1)+"%02d"%abs(i)+" "*(count)+"%02d"%abs(i))
cal(int(input()))
