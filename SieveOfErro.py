import math
def SieveErro(n):
    sieve = [True] * (n + 1)
    sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i] is True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve

def main():
    t = int(input())
    while t != 0:
        n = int(input())
        sieve = SieveErro(n + 1)
        for i in range(2, n + 1):
            if sieve[i] is True:
                print(i, end = ' ')
        t -= 1

if __name__ == '__main__':
    main()