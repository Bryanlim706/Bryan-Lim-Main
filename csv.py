#syntax practise


import csv

with open("favourites.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        favourite = row[1]
        print(f"favourite is {favourite}")


with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    Scratch, C, Python = 0, 0, 0

    for row in reader:
        favourite = row["language"]

        if favourite == "scratch":
            Scratch += 1

        elif favourite == "c":
            C += 1

        elif favourite == " Python


