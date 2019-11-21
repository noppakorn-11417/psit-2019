"""EZ"""
def main(head, leg):
    """EZ"""
    rabbit, false_witness = divmod(leg-2*head, 2)
    if rabbit >= 0 and head-rabbit >= 0 and false_witness == 0:
        print(rabbit, head-rabbit)
    else:
        print("Impossible")
main(int(input()), int(input()))
