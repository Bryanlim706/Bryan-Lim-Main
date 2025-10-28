test_cases = int(input())

for i in range(test_cases):
    array_size = int(input())
    array = list(map(int, input().split()))
    
    zeros_count = 0
    ones_count = 0
    for element in array:
        if element == 0:
            zeros_count += 1
        elif element == 1:
            ones_count += 1
    
    mex_sets = min(zeros_count, ones_count)
    score = 0
    score += 2 * mex_sets

    for _ in range(mex_sets):
        array.remove(0)
        array.remove(1)
    
    for element in array:
        if element == 0:
            score += 1
    
    for element in array:
        score += int(element)

    print(score)

