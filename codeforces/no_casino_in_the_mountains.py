number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    first_line = input().split()
    n = int(first_line[0])
    k = int(first_line[1])
    second_line = input().split()
    good_day_counter = int(0)
    hike_counter = 0
    #if break_counter = 1, he is on a break
    break_counter = 0
    for day in second_line:
        if break_counter == 1:
                break_counter = 0
                continue
        if break_counter == 0:

            if int(day) == 0:
                good_day_counter += 1
            else:
                 good_day_counter = int(0)
            if good_day_counter == k:
                good_day_counter = 0
                hike_counter += 1
                break_counter = 1

    
    print(hike_counter)



