amt_of_samples = int(input())
for _ in range(amt_of_samples):
    n = input()
    numbers = list(map(int, input().split()))
    count = len(set(numbers))
    candidates = [x for x in numbers if x >= count]
    ans = min(candidates)
    print(ans)