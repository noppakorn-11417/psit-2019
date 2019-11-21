"""EZ"""
def main(number_text, count=0):
    """EZ"""
    number = list(map(int, list(number_text)))
    for j in range(2, min(len(number), 11)):
        count += len([number[k:k+j] for k in range(len(number)) if sum(number[k:k+j]) == 10 \
        and len(number[k:k+j]) == j])
    print(count)
main(input())
