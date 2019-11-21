"""EZ"""
def main(number):
    """test"""
    ans_list = ["1", "2"]
    for _ in range(3, number+1):
        ans_list += [ans_list[-1]+ans_list[-2]]
    print(ans_list[number-1])
main(int(input()))
