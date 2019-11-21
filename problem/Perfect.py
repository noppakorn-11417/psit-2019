"""Perfect"""
def fast_factor(num):
    """fast factor v.2"""
    if str(num)[-1] not in "86":
        return 0
    return sum([i+(num//i) for i in range(2, int(num**0.5)+1) if num%i == 0])+1 == num
def main(num):
    """find connidate perfect number by Euler sol"""
    one, zero = "1", "0"
    i = 1
    num_bin = 0
    ans = 0
    while 1:
        num_bin = int(one*i+zero*(i-1), 2)
        if num_bin <= num:
            if fast_factor(num_bin):
                ans += num_bin
            i += 1
        else:
            break
    print(ans)
main(int(input()))
