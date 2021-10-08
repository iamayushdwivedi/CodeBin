def maxsumofSubArray(arr, k):
    maxSum = 0
    windowSum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(maxsumofSubArray(arr, k))