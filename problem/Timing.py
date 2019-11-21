"""pair"""
def main(secon):
    """clock"""
    day = secon//86400
    hour = secon%86400//3600
    minute = secon%86400%3600//60
    secon = secon%86400%3600%60
    print(day, hour, minute, secon)
main(int(input()))
