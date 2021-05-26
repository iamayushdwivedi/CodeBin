import math
def smallestSubarraywithgivenSum(arr, givenSum):
    minLength = math.inf
    windowSum = 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= givenSum:
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if minLength == math.inf:
        return 0
    return minLength

n = int(input())
givenSum = int(input())
arr = list(map(int, input().split()))
print(smallestSubarraywithgivenSum(arr, givenSum))