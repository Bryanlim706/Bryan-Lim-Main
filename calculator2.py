from cs50 import get_string

s = get_string("Do you agree? ")

if s == "Y" or s == "y":
    print("agreed.")

elif s == "N" or s == "n":
    print("disagreed.")
