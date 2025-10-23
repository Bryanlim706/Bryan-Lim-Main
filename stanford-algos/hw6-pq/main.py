from collections import defaultdict

x = 0

#hash function precursors
table_size = int((2 * 10**6) + 3)
hashed_array = [None] * table_size

#to track duplicates
duplicate_tracker = defaultdict(int)

#define hash function
def hash_function(x):
    index = (((x % table_size) + table_size) % table_size)
    start = index
    while True:
        if hashed_array[index] == None:
            hashed_array[index] = x
            duplicate_tracker[x] += 1
            return
        elif hashed_array[index] == x:
            duplicate_tracker[x] += 1
            return
     
        index = ((index + 1) % table_size)
        if index == start:
            raise Exception("Hash table full or loop detected.")
        
#define t set
t_set = set()
        
#load data into data_array
data_array = []
with open("data.txt", "r") as file:
    for line in file:
        number = int(line.strip())  # remove newline and convert to int
        data_array.append(number)

#lookup function
def lookup(x):
    index = (((x % table_size) + table_size) % table_size)
    start = index
    while True:
        if hashed_array[index] == x:
            return True
        elif hashed_array[index] == None:
            return False
        index = ((index + 1) % table_size)
        if index == start:
            return False
        
#add_t function
def add_t(x):
    t_set.add(x)

#MAIN
for number in data_array:
    hash_function(number)

for t in range(-10000, 10001):
    for number in data_array:
        y = t - number
        if lookup(y):
            if number != y or duplicate_tracker[number] >= 2:
                add_t(t)
                break  # Only need one valid x + y = t
    x += 1
    print(f"{(x / 20001) * 100:.2f}% complete")

print(len(t_set))

