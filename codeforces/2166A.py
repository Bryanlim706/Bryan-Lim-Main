cases = int(input())
for case in range(cases):
    length = int(input())
    word = list(input())
    counter = 0
    for i in range(length):
        if word[i] != word[length - 1]:
            counter += 1
    print(counter)
