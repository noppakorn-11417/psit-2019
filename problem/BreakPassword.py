"""ez"""
import hashlib
def main(password):
    """ez"""
    for i in range(0, 100000):
        i = "%05d"%i
        if str(hashlib.sha512(i.encode()).hexdigest().upper()) == password:
            print(i)
main(input())
