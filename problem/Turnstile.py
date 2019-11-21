"""psit"""
def main(inputs_1, inputs_2="", ans=0):
    """find mu for p duk"""
    while inputs_1 != "END":
        if inputs_1 == "P" and inputs_2 == "C":
            ans += 1
        inputs_1, inputs_2 = input(), inputs_1
    print(ans)
main(input(),)
