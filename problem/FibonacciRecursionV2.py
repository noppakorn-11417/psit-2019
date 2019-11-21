"""young drum and broke"""
def fibo_0(num1, num2, num3, count, listed):
    """nani sore"""
    if count == 3:
        listed.append(int(input()))
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    listed.append(num1)
    listed.append(num2)
    listed.append(num3)
    temp2, temp3 = num2, num3
    num1 = temp2+temp3
    num2 = temp2+temp3+num3
    num3 = temp2+temp3+num3+temp2+temp3
    if count < listed[0]:
        return fibo_0(num1, num2, num3, count+18, listed)
    print(listed[listed[0]+1])
fibo_0(0, 1, 1, 3, [])
