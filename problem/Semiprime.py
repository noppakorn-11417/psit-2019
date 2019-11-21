"""Ez"""
def prime(num):
    """main"""
    aws = True
    if num == 1:
        aws = False
    elif num == 2:
        aws = True
    elif num %2 == 0:
        aws = False
    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num%i == 0 and i != 1:
                aws = False
                break
    return aws
 
def semi_prime(num):
    """despacito"""
    ans = set()
    prime_table = [i for i in range(2, num+1) if prime(i)]
    for j in prime_table:
        for i in prime_table:
            number = i*j
            if number <= num:
                ans.add(number)
    print(len(ans))
semi_prime(int(input()))
