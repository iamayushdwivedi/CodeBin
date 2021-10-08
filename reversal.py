def revRight(arr, i, j):
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

def printArray(arr , n):
    for i in range(n):
        print(arr[i], end = ' ')
    print()

def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        revRight(arr, 0, k - 1)
        revRight(arr, k, n - 1)
        revRight(arr, 0, n - 1)
        printArray(arr, n)
        t -= 1

if __name__ == '__main__':
    main()