"""fc inw bas"""
def main(code):
    """fc inw bas"""
    code_list = []
    while code != "END":
        code_list.append(code[0:4])
        code = input()
    chk_list = []
    for i in sorted(set(code_list)):
        year = i[0:2]
        if year in chk_list:
            year = "--"
        print(year, int(i[2:4]), code_list.count(i))
        chk_list += [i[0:2]*(year != "--")]
main(input())
