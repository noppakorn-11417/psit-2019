"""fc inw bas"""
def main(set_input):
    """fc inw bas"""
    card_num = ([str(i) for i in range(2, 11)]+"J Q K A".split())*4
    card_type = ["S"]*13+["H"]*13+["D"]*13+["C"]*13
    print(*(set([(i+j) for i, j in zip(card_num, card_type)])-set_input))
main(set([input() for _ in range(51)]))
