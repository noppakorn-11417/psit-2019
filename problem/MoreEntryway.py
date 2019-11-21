"""pair"""
def main(count):
    """output"""
    print("Output_"+str(count))
    if count < 20:
        return main(count+1)
main(1)
