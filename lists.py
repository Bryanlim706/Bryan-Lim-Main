from cs50 import get_string

s = get_string("do you agree?\n")

if s in ["y", "yes"]:
    print("agreed.")

elif s in ["n", "no"]:
    print("disagreed.")


