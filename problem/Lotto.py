"""midterm"""
def main(lotto, money=0):
    """psit"""
    near = [(int(lotto[0])-1)+1000000*((int(lotto[0])-1) < 0), (int(lotto[0])+1)%1000000]
    money += 6000000*(lotto[6] == lotto[0])
    money += 2000*(lotto[6][4:6] == lotto[1])
    money += 4000*((lotto[6][0:3] == lotto[2])+(lotto[6][0:3] == lotto[3]))
    money += 4000*((lotto[6][3:6] == lotto[4])+(lotto[6][3:6] == lotto[5]))
    money += 100000*((int(lotto[6]) == near[0])+(int(lotto[6]) == near[1]))
    print(money)
main([input() for i in range(7)])
