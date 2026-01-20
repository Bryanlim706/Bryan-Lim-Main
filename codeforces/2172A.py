arr = list(map(int, input().split()))
len = len(arr)
arr.sort()
difference = arr[(len - 1)] - arr[0]
if len % 2 == 0:
    median = (arr[len/2 - 1] + arr[len/2]) * 0.5
else:
    median = arr[int((len - 1) * 0.5)]
if difference >= 10:
    print("check again")
else: 
    print(f"final {median}")