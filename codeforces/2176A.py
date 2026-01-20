amt_of_samples = int(input())
for _ in range(amt_of_samples):
    input()
    numbers = input().split()
    max_number = 0
    new_list = []
    for i in range(len(numbers)):
        if int(numbers[i]) >= int(max_number):
            max_number = int(numbers[i])
            new_list.append(numbers[i])
    print(len(numbers) - len(new_list))
