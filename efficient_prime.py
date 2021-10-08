import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        for i in range(2, n + 1):
            if isPrime(i):
                print(i, end = ' ')
        print()
        t -= 1

if __name__ == '__main__':
    main()