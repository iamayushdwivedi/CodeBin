import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    n, k = map(int, input().split())
    for i in range(n):
        r = int(input())
        last = r % 10
        first = r // 10
        if isPrime(last):
            if isPrime(first):
                if (first + last) > k:
                    print("Yes")
        else:
            print("No")
if __name__ == '__main__':
    main()
