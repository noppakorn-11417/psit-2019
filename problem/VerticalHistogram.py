"""psit"""
def main(text):
    """fibo"""
    data_his = [(i, text.count(i)) for i in sorted(list(set(text)), key=str.swapcase)]
    max_data = max([data_his[i][1] for i in range(len(data_his))])
    for i, j in enumerate(range(max_data)):
        print("%03d "%(max_data-i), end="")
        for k in range(len(data_his)):
            if data_his[k][1] >= max_data-j:
                print("*", end="")
            else:
                print(" ", end="")
            print(" ", end="")
        print()
    print("    ", end="")
    for i in range(len(data_his)):
        print("%s "%(data_his[i][0]), end="")
main(input())
