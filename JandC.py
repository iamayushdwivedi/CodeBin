arr = [4, 6, 8, 5, 3, 10, 9]
for i in range(len(arr) + 1):
  if arr[i - 1] < arr[i]:
    arr.remove(arr[i + 1])
print(len(arr))