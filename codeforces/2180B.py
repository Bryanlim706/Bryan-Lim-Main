amt_of_samples = int(input())

for _ in range(amt_of_samples):
    input()    
    words = input().split()
    new_word = ""
    for word in words:
        candidate = word + new_word
        reverse_candidate = new_word + word
        if new_word == None or candidate < reverse_candidate:
            new_word = candidate
        else:
            new_word = reverse_candidate
    print(new_word)