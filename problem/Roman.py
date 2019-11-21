"""EZ"""
def roman(text):
    """EZ"""
    sum_roman = 0
    roman_special = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    roman_list = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in roman_special:
        if i in text:
            sum_roman += text.count(i)*roman_special[i]
            text = text.replace(i, "")
    for i in roman_list:
        if i in text:
            sum_roman += text.count(i)*roman_list[i]
            text = text.replace(i, "")
    print(sum_roman)
roman(input())
