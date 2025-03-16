from cs50 import get_string

people = {
    "Carter": +100 ,
    "David": +99 ,
    "John": +98 ,
}

name = get_string("name: ")
if name in people:
    print(f"number: {people[name]}")
else:
    print("not found")
