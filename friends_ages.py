'''n = int(input())
count = 0
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if i != j:
            if ((arr[j] <= 0.5*arr[i] + 7) or (arr[j] > 100 and arr[i] < 100) or (arr[j] > arr[i])):
                continue
            else:
                count += 1
print(count)'''
n = int(input())
arr = list(map(int, input().split()))
freq = [0]*121
ans = 0
for i in range(n):
    freq[arr[i]] += 1

for i in range(1, 121):
    for j in range(1, 121):
        if i <= 0.5*j+7:
            continue
        if i > 100 and j < 100:
            continue
        if i > j:
            continue
        ans += freq[i] * freq[j]
        if i == j:
            ans -= freq[i]
print(ans)