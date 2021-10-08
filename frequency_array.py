n = int(input())
arr = list(map(int, input().split()))
freq = [0] * 40
for i in range(n):
    freq[arr[i]] += 1
for i in range(n):
    print(max(freq[arr[i]]) - min(freq[arr[i]]))
    break
