"""psit"""
def circular(list_split, listed, chk=1):
    """love p nour"""
    if set(list_split)-{"1", "3", "7", "9"} != set() and list_split > "5":
        return 0
    for _ in range(len(list_split)):
        list_split = list_split[1:]+list_split[0]
        chk *= listed[int(list_split)]
    return list_split*chk
 
def main(number, pin=2):
    """i sleep"""
    prime_table = [True]*((10**(len(str(number))))+1)
    while pin**2 <= (10**((len(str(number))))+1):
        if prime_table[pin] == True:
            for i in range(pin*2, (10**(len(str(number))))+1, pin):
                prime_table[i] = False
        pin += 1
    prime_num = [i for i in range(2, number+1) if prime_table[i]]
    prime_cir = [circular(str(i), prime_table) for i in prime_num]
    prime_cir = [int(i) for i in prime_cir if i != ""]
    print(sum(prime_cir))
main(int(input()))
