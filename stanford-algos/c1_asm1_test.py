import sys
import math

# Check if the number length is a power of 2
def is_power_of_2(n):
    return (math.log(n, 2) % 1 == 0)

X = input("First Number: ")
Y = input("Second Number: ")

# Ensure both numbers are valid and have equal lengths
if not X or not Y:
    print("Missing input")
    sys.exit()

elif len(X) != len(Y):
    print("Length of numbers not equal")
    sys.exit()

elif len(X) % 2 != 0:
    print("Numbers are not of even length")
    sys.exit()

elif not is_power_of_2(len(X)) or not is_power_of_2(len(Y)):
    print("Not a 2^n length number")
    sys.exit()

def karatsuba_multiply(x, y):
    # Base case: if the numbers are single digits
    if x < 10 and y < 10:
        return x * y

    # Convert numbers to strings
    strx, stry = str(x), str(y)
    n = len(strx)
    half_n = n // 2  # Divide the numbers into two halves

    # Split the numbers into high and low parts
    x1 = int(strx[:half_n])
    x0 = int(strx[half_n:])
    y1 = int(stry[:half_n])
    y0 = int(stry[half_n:])

    # Recursively apply Karatsuba algorithm
    p1 = karatsuba_multiply(x1, y1)
    p2 = karatsuba_multiply(x0, y0)
    p3 = karatsuba_multiply(x1 + x0, y1 + y0)

    # Combine the results using the Karatsuba formula
    return p1 * (10 ** (2 * half_n)) + ((p3 - p1 - p2) * (10 ** half_n)) + p2

# Convert inputs to integers
result = karatsuba_multiply(int(X), int(Y))
print(f"Answer : {result}")


karatsuba_multiply(x1 + x0, y1 + y0)

8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184

x1 = int(strx[:half_n])
        x0 = int(strx[half_n:])
        y1 = int(stry[:half_n])
        y0 = int(stry[half_n:]) 

return int(p1 * (10 ** (2 * half_n)) + ((p3 - p1 - p2) * (10 ** (half_n))) + p2)

karatsuba_multiply(x1 + x0, y1 + y0)