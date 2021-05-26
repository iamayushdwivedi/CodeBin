def rotateArray(lists, num):
    output_list = []
    for i in range(len(lists) - num, len(lists)):
        output_list.append(lists[i])

    for i in range(0, len(lists) - num):
        output_list.append(lists[i])

    x = str(output_list)[1:-1]
    x = x.replace(',', ' ')
    return x

def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(rotateArray(arr, k))
        t -= 1

if __name__ == '__main__':
    main()