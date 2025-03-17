#karatsuba algorithm for two equal and 2**n length numbers
import sys
import math

X = input("First Number: ")
Y = input("Second Number: ")

if not X or not Y:
    print("Missing input")
    sys.exit()

elif len(X) != len(Y):
    print("length of numbers not equal")
    sys.exit()

elif len(X) % 2 != 0:
    print("Numbers are not of even length")
    sys.exit()

elif not math.log(float(len(X)), 2) % 1 == 0 or not math.log(float(len(Y)), 2) % 1 == 0:
    print("not a 2^n length number")
    sys.exit()

def karatsuba_multiply(x, y):
    strx, stry = str(x), str(y)
    if x > y:
        n = len(strx)
    else:
        n = len(stry)

    if n != 1 and n != 0:
        half_n = math.ceil(n / 2)
        if n > len(strx):
            x1 = 0
            x0 = x
        else:
            x1 = int(strx[:half_n])
            x0 = int(strx[half_n:])
        if n > len(stry):
            y1 = 0
            y0 = y
        else:
            y1 = int(stry[:half_n])
            y0 = int(stry[half_n:])
        
        p1 = karatsuba_multiply(x1, y1)
        p2 = karatsuba_multiply(x0, y0)
        p3 = karatsuba_multiply(x1 + x0, y1 + y0)

        half_n = n // 2
        return int(p1 * (10 ** (2 * half_n)) + ((p3 - p1 - p2) * (10 ** (half_n))) + p2)
    else:
        return int(x * y)

print(f"Answer : {karatsuba_multiply(int(X), int(Y))}")