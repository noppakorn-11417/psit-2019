"""psit"""
def main(num):
    """find mu for p duk"""
    print("%.2f"%(((num+(50 if num*0.1 < 50 else 1000 if num*0.1 > 1000 else num*0.1))*1.07)))
main(int(input(),))
