"""fc inw bas"""
def main(x_x):
    """fc inw bas"""
    for i in [(i, x_x.count(i)) for i in sorted(list(set(x_x)), key=str.swapcase)]:
        bar1 = ((i[1] > 5 and i[1]%5 != 0)*"|"+(i[1]%5)*"-")
        print("%s : %s"%(i[0], "|".join((i[1]//5*"----- ").split())+bar1))
main(list(input()))
