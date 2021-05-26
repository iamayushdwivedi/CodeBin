'''n = int(input())
k = int(input())
arr = list(map(int, input().split()))
sum = 0
max = -1
for i in range(0, n-k+1):
    sum = 0
    for j in range(i, i + k):
       sum += arr[j]
       if sum > max:
           max = sum

print(max)'''
#sliding window technique
n = int(input())
k = int(input())
arr = list(map(int, input().split()))
sum = 0
max = -1
for i in range(0, k):
    sum += arr[i]
for j in range(k, n):
    sum = sum - arr[j-k] + arr[j]
    if sum > max:
        max = sum
print(max)
'''def avgofSubarray(arr, k):
    result = []
    sum = 0
    i = 0
    for j in range(len(arr)):
        sum += arr[j]
        if j >= k-1:
            result.append(sum/k)
            sum -= arr[i]
            i += 1
    return result

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
print(avgofSubarray(arr, k))'''