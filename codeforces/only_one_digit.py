amt_of_test_cases = int(input())

for i in range (amt_of_test_cases):
    number = str(input())
    digits = [int(d) for d in number]
    smallest_number = float('inf')
    for digit in digits:
        if digit < smallest_number:
            smallest_number = digit
    print(smallest_number)

